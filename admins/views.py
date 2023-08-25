from django.shortcuts import render,redirect,get_object_or_404
from .forms import JobForm
from .models import Job
# Create your views here.

def admin(request):
    objects = Job.objects.all()

    return render(request, 'admins/admin.html',{'jobs':objects})


def job_post(request):
    if request.method == 'POST':
        form = JobForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin')
        else:
            print('eroorrr')
    else:
        form = JobForm()
        
    return render(request, 'admins/job_post.html', {'form': form})    


def update_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('admin')  
    else:
        form = JobForm(instance=job)
    return render(request, 'admins/job_post.html', {'form': form})

def delete_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    print("outside working")
    if request.method == 'POST':
        print("working")
        job.delete()
        return redirect('admin')  
    return render(request, 'admins/delete_job.html', {'job': job})
