import requests
import time
from bs4 import BeautifulSoup
import pandas as pd


url='https://www.indeed.co.in/jobs?q=python+developer&l=Chennai%2C+Tamil+Nadu'

response=requests.get(url)

soup=BeautifulSoup(response.text,'html.parser')


name=soup.find_all('div',class_='result')

job_title=[]

company=[]

place=[]

money=[]

summary=[]


# Job title
for n in name:
    title=n.find_all('div',class_='title')
    for i in title:
        add=i.a.text.strip()
        job_title.append(add)
# Company name
for n in name:
    title=n.find_all('div',class_='sjcl')
    for i in title:
        add=i.div.span.text.strip()
        company.append(add)

# location   
for n in name:
    title=n.find_all('div',class_='location accessible-contrast-color-location')
    for i in title:
        address=i.text.strip()
        place.append(address)
if len(place)<len(company):
    for i in range(len(company)-len(place)):
        place.append("Not mention")

# salary
for n in name:
    title=n.find_all('div',class_='salarySnippet salarySnippetDemphasizeholisticSalary')
    for i in title:
        salary=i.span.text.strip()
        money.append(salary)
if len(money)<len(company):
    b=len(company)-len(money)
    for i in range(b):
        money.append("Not_mentioned")
        

# summary
for n in name:
    title=n.find_all('div',class_='summary')
    for i in title:
        para=i.text.strip()
        summary.append(para)

# converting into order

data={
    'Job_title':job_title,
    'company_name':company,
    'Location':place,
    'salary':money,
    'Job_summary':summary,
}

df=pd.DataFrame(data,columns=['Job_title','company_name','Location','salary','Job_summary'])

# creating csv file

df.to_csv('indeed_joblist.csv')
