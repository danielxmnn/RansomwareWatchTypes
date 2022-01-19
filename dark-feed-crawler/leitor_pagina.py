import requests
from bs4 import BeautifulSoup
import sqlite3 as sl
import send
import time

con = sl.connect('base.db')
cur = con.cursor()
headers = {
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'Referer': 'https://darkfeed.io/feed/',
    'DNT': '1',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/96.0.4664.110 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}
page = requests.get('https://darkfeed.io/indexransomware/', headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
MoblieDetails = []
for text in soup.find_all('article'):
    b = text
    a = b.get_text()
    MoblieDetails.append(a.splitlines())
x = 0
y = len(MoblieDetails)
saida = []
while x < y:
    aux = [i for i in MoblieDetails[x] if i]
    x += 1
    j = 0
    k = len(aux)
    while j < k:
        aux2 = aux[j].replace("\t", "")
        saida.append(aux2)
        j += 1

auxi = 0
while auxi + 2 < len(saida):
    cur = cur.execute("SELECT * FROM projects WHERE victim='"+str(saida[auxi+2])+"' ")
    result = cur.fetchone()
    if not result:
        print(str(saida[auxi + 2]))
        time.sleep(10)
        send.main(str(saida[auxi]), str(saida[auxi + 1]), str(saida[auxi + 2]))
        con.execute("INSERT INTO projects VALUES  (\"%s\",\"%s\",\"%s\")""" % (
            str(saida[auxi]), str(saida[auxi + 1]), str(saida[auxi + 2])))
    auxi += 3
con.commit()
con.close()
