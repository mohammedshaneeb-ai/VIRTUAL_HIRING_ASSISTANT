from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import pandas as pd
from pandasai import PandasAI
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import zipfile
import os
import requests
from decouple import config
import csv
from home.models import Candidate

from pandasai.llm.openai import OpenAI

OPENAI_API_KEY = config('OPENAI_API_KEY')
llm = OpenAI(api_token=OPENAI_API_KEY)

# Create your views here.
def chat_home(request):
    return render(request,'chat/chat.html')


def chat(request):
    if request.method == "POST":
        msg = request.POST.get("msg")
        print(msg)
        print(type(msg))
        response = get_Chat_response(msg,request)
        return JsonResponse({"response": response})
    
def get_Chat_response(text,request):
    df = pd.read_csv('http://127.0.0.1:8000/admin/chat_home/export-csv/')

    pandas_ai = PandasAI(llm)
    print("the promt is :",text)

    response = pandas_ai(df, prompt=text)

    if isinstance(response, plt.Figure):
        print("matplotlib output")
        buf = BytesIO()
        response.savefig(buf, format='png')
        response_image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
        response_image_html = f'<img src="data:image/png;base64,{response_image_base64}">'
        return response_image_html
    elif isinstance(response, pd.DataFrame):
        print("Dataframe output")
        if 'resume_link' in response.columns:
            resume_links_list = response['resume_link'].tolist()
            zip_buffer = BytesIO()
        zip_file_name = "all_resumes.zip"
        if 'name' in response.columns:
            with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zipf:
                for link in resume_links_list:
                    print(link)
                    file_name = os.path.basename(link)
                    row = response[response['resume_link'] == link]
                    print(response['resume_link'])
                    if not row.empty:
                        resume_name = row.iloc[0]['name']
                        print('Resume name:::::::::::',resume_name)
                        file_content = requests.get(link).content
                        zipf.writestr(f"{resume_name}.pdf", file_content)  # Save with resume name
                    else:
                        # Fallback to using the original file name
                        print('this is working')
                        file_content = requests.get(link).content
                        zipf.writestr(file_name, file_content)
            
            def make_clickable(val):
                filename = os.path.basename(val)
                # link_number = int(filename.split("_")[1])  # Assuming your link is named something like "resume_1.pdf"

                if 'name' in response.columns:
                    row = response[response['resume_link'] == val]
                    if not row.empty:
                        link_name = row.iloc[0]['name']
                        return f'<a href="{val}" download="{filename}">{link_name}</a>'
                return f'<a href="{val}">{val}</a>'
    
            response['resume_link'] = response['resume_link'].apply(make_clickable)
            

            # zip_file_name = "resumes.zip"
            # zip_buffer = BytesIO()
            # with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zipf:
            #     for link in resume_links_list:
            #         file_name = os.path.basename(link)
            #         file_content = requests.get(link).content  # You may need to import requests
            #         zipf.writestr(file_name, file_content)     
        





        

        response_table_html = response.to_html(escape=False, render_links=True)
        
        response_html = f'<div>{response_table_html}</div>'
        response_html += f'<a href="data:application/zip;base64,{base64.b64encode(zip_buffer.getvalue()).decode()}" download="{zip_file_name}">Download All Resumes as Zip</a>'

        return response_html

    else:
        print('string')
        return str(response)
    


def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="home_candidate.csv"'

    writer = csv.writer(response)
    writer.writerow(['id', 'name', 'place', 'score', 'domain','resume_link','email','phone','age','experience','education','skills'])  # Write header row

    candidates = Candidate.objects.all()  # Fetch data from the model
    for candidate in candidates:
        writer.writerow([candidate.id, candidate.name, candidate.place, candidate.score, candidate.domain, candidate.resume_link, candidate.email, candidate.phone, candidate.age, candidate.experience, candidate.education, candidate.skills ])  # Write data rows

    return response