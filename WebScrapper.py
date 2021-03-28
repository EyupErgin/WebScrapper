
import sys
from requests import get
from fuzzywuzzy import fuzz
from bs4 import BeautifulSoup
from googlesearch import search
from colorama import Fore, Back, Style, init

init(autoreset=True)


export = "--save" in sys.argv


print("""
Project Name : WebScrapper
Created : https://github.com/EyupErgin
Github  : https://github.com/IntelSights/WebScrapper/
""")

query = input(Fore.WHITE + 'Enter Dork : ' + Fore.WHITE)
results = 5000


print(Fore.WHITE + 'Scanning > ' + query)
for url in search(query, stop = results):
	print('\n' + Fore.GREEN + '[+] URL Detected : ' + Fore.WHITE+  url)
	if export:
		with open(query + ".txt", "a") as file:
			file.write(url + "\n")
	try:
		text = get(url, timeout = 1).text
	except:
		continue
	soup = BeautifulSoup(text, "html.parser")
	links_detected = []
	try:
		print(Fore.GREEN + '[+] Title: ' + Fore.WHITE + soup.title.text.replace('\n', ''))
	except:
		print(Fore.RED + '[-] Title: Title not found')

	try:
		for link in soup.findAll('a'):
			href = link['href']
			if not href in links_detected:
				if href.startswith('http'):

					if url.split('/')[2] in href:
						links_detected.append(href)

					elif query.lower() in href.lower():
						print(Fore.GREEN + '[+] Founds : ' + href)
						links_detected.append(href)
						if export:
							with open(query + ".txt", "a") as file:
								file.write(href + "\n")

					elif fuzz.ratio(link.text, href) >= 60:
						print(Fore.GREEN + '[/] Similar Text and Links : ' + href)
						links_detected.append(href)
						if export:
							with open(query + ".txt", "a") as file:
								file.write(href + "\n")
	except:
		continue
	if links_detected == []:
		print(Fore.RED + '[-] Internal Data Not Found')


