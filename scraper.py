from bs4 import BeautifulSoup as bs
import requests
import pandas as pd


url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

page = requests.get(url, verify=False)
print(page)

soup = bs(page.text,'html.parser')

star_table = soup.find_all('table')

temp_list= []
table_rows = star_table[4].find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

names = []
distance =[]
mass = []
radius =[]


for i in range(1,len(temp_list)):
    
    names.append(temp_list[i][0])
    distance.append(temp_list[i][5])
    mass.append(temp_list[i][7])
    radius.append(temp_list[i][8])

df = pd.DataFrame(list(zip(names,distance,mass,radius)),columns=['Star_Name','Distance','Mass','Radius'])
print(df)

df.to_csv('dwarf_stars.csv')