import requests
import bs4

url = "https://lv.wikipedia.org/wiki/R%C4%ABgas_Tehnisk%C4%81_universit%C4%81te"
saturs=requests.get(url)

if satrurs.status_code==200:
    lapas_saturs=bs4.BeautifulsSoup(saturs.content, 'html.parser')
    atradu=lapas_saturs.find_all(class_="interlanguage-link")
    res=[]
    for a in atradu:
        row = a.findChild("a")
        res.append(row)

    for ieraksts in res:
        row=[]
        valoda = ieraksts.attrs['title']
        row.append(valoda)
        row.append(lang)
        dati.append(row)

print(dati)