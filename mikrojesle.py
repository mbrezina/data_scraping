import requests
import json
import csv
import re

r = requests.get("https://mikrojesle.mpsv.cz/index.php/zrizovatele-mikrojesli/")
#print(r.text)
start = r.text.find("Hlavní město Praha") -20
#print(start)
konec = r.text.find("</div></div></div></div>")  -299
#print(konec)
#print(r.text[start:start])
#print(r.text[konec:konec])

vyrez = r.text[start:konec] 
#print(vyrez)


""" Pokus o reguláry
Název, Group1  <p><strong>([a-zA-Z0-9\s*])</strong><br />
Adresa, Group2, 
E-mail, Group3, 
"""

#Ondrův kód, upraven
vysledek = ""
soubor = open("mikroj.csv", "w", encoding="utf-8")
seznam = ["id\t" ,"Označení:\t", "Adresa1:\t", "Adresa2:\t", "Adresa3:\t", "Zahájení provozu:\t", "Email:\t"]
soubor.write('\t'.join(seznam)+"\n")

pattern = re.compile(r"<p><strong>(.*)</strong><br />\n(.*)<br />\n(.*)<br />\n(.*)<br />\n(.*)<br />\n(.*)</p>")

"""
for m in re.finditer(pattern, vyrez):
	vysledek += '' .join ((f"klic:{m.group(1)}\nhodnota: {m.group(2)}\nhodnota: {m.group(3)}\nhodnota: {m.group(4)}\n-----"))
""" 

index = 1
for m in re.finditer(pattern, vyrez):
	hodnota = m.group(1)
	vysledek += hodnota +"\t"
	hodnota = m.group(2)
	vysledek += hodnota +"\t"
	hodnota = m.group(3)
	vysledek += hodnota +"\t"
	hodnota = m.group(4)
	vysledek += hodnota +"\t"
	hodnota = m.group(5)
	vysledek += hodnota +"\t"
	hodnota = m.group(6)
	vysledek += hodnota +"\t"
	soubor.write("MJ"+str(index)+"\t"+vysledek+"\n")
	#print(vysledek)
	index += 1
	vysledek = ''	

soubor.close()




