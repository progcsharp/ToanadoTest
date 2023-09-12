import requests
from bs4 import BeautifulSoup

from app.db.hendlers.create import create_collect_data
from app.db.hendlers.delete import delete_collect_data

delete_collect_data()

r = requests.get("https://en.wikipedia.org/wiki/Python_(programming_language)#Typing")
s = r.text
soup = BeautifulSoup(s, "html.parser")
table = soup.find("table", attrs={"class":"wikitable"})
table_body = table.find('tbody')
rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    if cols:
        print(cols)
        create_collect_data(cols)

# s = '\'Wikipedia\'"Wikipedia""""Spanning\nmultiple\nlines"""\nSpanning\nmultiple\nlines'
# print(s)
# for i in s:
#     if i == '\n':
#         s.replace("\n", "")
# 
# print(s)
