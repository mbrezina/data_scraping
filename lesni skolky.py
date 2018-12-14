import requests
import json
import csv

vysledek = ""

r = requests.get('http://lesnims.cz/lesni-ms/mapa-lesnich-ms.html')
start = r.text.find("mapData") + 32
print(start)
konec = r.text.find("<!-- Main -->")  -32
print(konec)
print(r.text[start:start+50])
print(r.text[konec-50:konec])

vyrez = r.text[start:konec]
skolky = json.loads(vyrez)
#print(skolky)

seznam = ["index;", "Označení:;", "Adresa:;", "Email:;", "Souřadnice A:;", "Souřadnice B:;"] 

soubor = open("lesni.csv", "w", encoding="utf-8")
soubor.write('\t'.join(seznam)+"\n")
index = 1

for skolka in skolky:
	vysledek += ("LS{}; {}; {}; {}; {}; {} \n".format(index, skolka["C"], skolka["D"], skolka["E"], skolka["A"], skolka["B"])) 
	#vysledek.append("ls" + str(index) + ";"+vysledek
	index += 1

soubor.write(vysledek)
soubor.close()
