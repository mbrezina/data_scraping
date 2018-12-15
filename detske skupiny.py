import requests
import csv
import re

r = requests.get('http://evidence.mpsv.cz/eEDS/index.php?search')
start = r.text.find("prehledDiv") +105
konec = r.text.find("</table><br/></div><br /><br />")

vysledek = ""
seznam = ["index:", "Označení:", "Kapacita:", "Adresa", "Místo poskytování služby:", "Pozastavení / zánik oprávnění:"]
vyrez = r.text[start:konec]
pattern = re.compile(r"<tr><td class='txtRight fixWidth'>(.*)</td><td class='txtLeft padLeft10'><b>(.*)</b></td></tr>")
soubor = open("dets.csv", "w", encoding="utf-8")
hotovo = []
soubor.write('\t'.join(seznam)+"\n")
index = 1

for m in re.finditer(pattern, vyrez):
	klic = m.group(1)
	hodnota = m.group(2)
	if klic in seznam:
		if klic != "Místo poskytování služby:":
			vysledek += hodnota +"\t"
		else:
			vysledek += hodnota[hodnota.find(">")+1:-4] +"\t"
		if klic == "Pozastavení / zánik oprávnění:":
			soubor.write("DS"+str(index)+"\t"+vysledek+"\n")
			vysledek = ''
			index += 1

soubor.close()
