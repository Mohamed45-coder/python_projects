import requests 
from bs4 import BeautifulSoup
import pandas as pd 

url='https://www.cricketworldcup.com/standings'

response=requests.get(url)

soup=BeautifulSoup(response.text,'html.parser')

table_point=soup.find('table',class_='table')

pos=[]
team=[]
won=[]
played=[9,9,9,9,9,9,9,9,9,9]
score=[]

for table in table_point.find_all('tbody'):
    rows=table.find_all('tr')
    for row in rows:
        point=row.find('td',class_='table-body__cell table-body__cell--position').text
        count=row.find('td',class_='table-body__cell table-body__cell--main').find('span',class_='u-hide-phablet table-link-text').text.strip()
        win=row.find('td',class_='table-body__cell u-hide-phablet').text.strip()
        pts=row.find('td',class_='table-body__cell table-body__cell--points').text.strip()

        pos.append(point)
        team.append(count)
        won.append(win)
        score.append(pts)

data={
    'Position':pos,
    'Countries':team,
    'Matches_played':played,
    'Matches_won':won,
    'Point_table':score,
}

df=pd.DataFrame(data,columns=['Position','Countries','Matches_played','Matches_won','Point_table'])

print(df)

df.to_csv('cricket_score_table.csv')