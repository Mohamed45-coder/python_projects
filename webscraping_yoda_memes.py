import requests
from bs4 import BeautifulSoup
import os 
import time



response=requests.get('https://www.boredpanda.com/baby-yoda-memes/?utm_source=google&utm_medium=organic&utm_campaign=organic')

soup=BeautifulSoup(response.content,'html.parser')

img_ls=soup.find_all("img",class_='image-size-full')

link_list=[]
n=1
for i in img_ls:
    if n<=5:
        link_list.append(i['src'])
        time.sleep(1)
    else:
        break
    n+=1
os.chdir('image_folder')

for index,link in enumerate(link_list):
    data=requests.get(link).content
    with open("image_folder/"+str(index)+('.jpg'),'wb') as create:
        create.write(data)

