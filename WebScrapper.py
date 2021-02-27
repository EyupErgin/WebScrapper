#İç Yapı = Part1
import sys
from requests import get
from fuzzywuzzy import fuzz
from bs4 import BeautifulSoup
from googlesearch import search
from colorama import Fore, Back, Style, init

init(autoreset=True)

#Modüller = Part2
saveInFile = "--save" in sys.argv

print("""
###      ###  _____         _    ___     _     _   
#	 o # |_   _|  _ _ _| |__/ _ \ __(_)_ _| |_ 
	       | || || | '_| / / (_) (_-< | ' \  _|
               |_| \_,_|_| |_\_\\___//__/_|_||_\__|
#	   # Proje Adı: https://github.com/TurkOsint
###      ### Kodlayan : https://github.com/EyupErgin
""")

query = input(Fore.WHITE + '[TurkOsint] Taranacak Kelimeleri Giriniz > ' + Fore.WHITE)
results = 10000

#Modüller = Part3
print(Fore.WHITE + '[TurkOsint] Taranıyor > ' + query)
for url in search(query, stop = results):
	print('\n' + Fore.GREEN + '[+] Url Tespit Edildi: ' + Fore.WHITE+  url)
	if saveInFile:
		with open(query + ".txt", "a") as file:
			file.write(url + "\n")
	try:
		text = get(url, timeout = 1).text
	except:
		continue
	soup = BeautifulSoup(text, "html.parser")
	links_detected = []
	try:
		print(Fore.GREEN + '[+] Başlık: ' + Fore.WHITE + soup.title.text.replace('\n', ''))
	except:
		print(Fore.RED + '[-] Başlık: Başlık Bulunamadı')
#Modüller = Part4
	try:
		for link in soup.findAll('a'):
			href = link['href']
			if not href in links_detected:
				if href.startswith('http'):
#Modüller = Part5
					if url.split('/')[2] in href:
						links_detected.append(href)
#Modüller = Part6
					elif query.lower() in href.lower():
						print(Fore.GREEN + '[/] Bulunanlar : ' + href)
						links_detected.append(href)
						if saveInFile:
							with open(query + ".txt", "a") as file:
								file.write(href + "\n")
#Modüller = Part7
					elif fuzz.ratio(link.text, href) >= 60:
						print(Fore.GREEN + '[/] Benzer Metin ve Bağlantılar : ' + href)
						links_detected.append(href)
						if saveInFile:
							with open(query + ".txt", "a") as file:
								file.write(href + "\n")
	except:
		continue
	if links_detected == []:
		print(Fore.RED + '[-] İç Veri Bulunamadı')


