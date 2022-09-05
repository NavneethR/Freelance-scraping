import requests
import win10toast
from bs4 import *

html = BeautifulSoup(requests.get("https://www.freelancer.com/job-search/projects/?projectLanguages=en").content,"html.parser")
Toaster = win10toast.ToastNotifier()
req_skills = ["Python"]
all_jobs = []
valid_jobs = []
job_num = 1

def add_job(job):
    global all_jobs,job_num
    skills = []
    for skill in job.find_all(class_ = "JobSearchCard-primary-tagsLink"):
        skills.append(skill.text)
    descr = job.find("p",class_ = "JobSearchCard-primary-description").text.strip()
    job = job.find("a").text.strip()
    skill = skills
    all_jobs.append([job,descr,skill])
  
def validate_job(all_jobs):
    for job,descr,skill in all_jobs:
        for req_skill in req_skills:
            if req_skill in skill:
                valid_jobs.append([job,descr,skill])
    return valid_jobs
        
def send_message():
    Toaster.show_toast("Hello World!!!","Python is 10 seconds awsm!")

for job in html.find_all(class_ = "JobSearchCard-primary"):
    add_job(job)

for job in validate_job(all_jobs):
    Toaster.show_toast(job[0],job[1])

