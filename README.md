
# VIRTUAL HIRING ASSISTANT

This project is helpful for both HR's and candidate's who is applying for job

## What is the problem this project is solving
#### In HR side:

 if a HR is post a job in any job portal,then HR will get many application. so it is diffucult to setup call for every one who applied. to solve this problem i made a VIRTUAL HIRING ASSISTANT for HR.

#### In Candidate Side:

 if a candidate is going to apply job,he/she want to enter many details and upload the resume.so here many manual work is happening this is very time consuming thing.to resolve this issue i made a Machine Learning model for extracting useful information from resume.


 ## What  VIRTUAL HIRING ASSISTANT does
 #### for HR:
The HR can ask any questions related to his databse. 

```
- Shortlist the candidates who scored more than 87% in Data Science domain with atleast 3 years of experience
- how many are applied for Data Engineer
- Plot a graph of domains with number of applicants
- how many are from Data Science domain with age more than 30

```
Now the HR will get answer in many formats.if the answer in table format the result will display in table format,if the answer in integer format the result will display in integer format.if the answer in graph format the result will display in matplotlib image

#### for Candidate:
The candidate only want to upload his resume the my Machine Learning model will extract all useful informations like  __name__,__email__,__place__,__phone__,__education__,__skills__,etc.  
the extracted information show in another page so the candidate can edit the details when need and submit.  
the user can also see his score(similarity score of skills in resume and JD),so he can improve his resume.

## Stacks Used
* PandasAI
* Django
* Spacy for NER
* Firebase 
* MySQL
* AWS ec2

## Special Features
* Skill extraction
* Chatbot 

## The Challenges 
 - Availability of real resumes for training NER model
 