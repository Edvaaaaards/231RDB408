import requests
import bs4

url = "https://lv.wikipedia.org/wiki/R%C4%ABgas_Tehnisk%C4%81_universit%C4%81te"
saturs=requests.get(url)

if satrurs.status_code==200:
    lapas_saturs=bs4.BeautifulsSoup(saturs.content, 'html.parser')
    atradu=lapas_saturs.find_all(class_="application/ld+json")
    for a in atradu: 
        print(a.string)
        