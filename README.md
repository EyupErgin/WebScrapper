<p align="center">
  <img src="https://github.com/IntelSights/About/blob/main/img/IntelSights.png?raw=true" alt="IntelSights" width="250" />
</p>

<h1 align="center">WebScrapper</h1>

It is a tool written for digging data on the web.

<h2 align="left">Features:</h2>

- [x] Save Data
- [x] Dork Support
- [x] Website URL
- [x] Website Title
- [x] Website Info
- [x] PDF Text Scanner


<h2 align="left">Installing:</h2>

```
git clone https://github.com/IntelSights/WebScrapper.git
```

<h2 align="left">Using:</h2>

```
cd WebScrapper/

pip3 install -r requirements.txt

python3 WebScrapper.py  

```

<h2 align="left">Example:</h2>

<h3 align="left">Example 1 : Basic</h2>

```
python3 WebScrapper.py  

Output;

Enter Dork : Bill Gates
Scanning > Bill Gates

[+] URL Detected : https://www.gatesnotes.com/
[+] Title: Access Denied
[-] Internal Data Not Found

[+] URL Detected : https://en.wikipedia.org/wiki/Bill_Gates
[+] Title: Bill Gates - Wikipedia
```

<h3 align="left">Example 2 : Dork</h2>

```
python3 WebScrapper.py  

Output;

Enter Dork : site:eyupergin.com
Scanning > site:eyupergin.com

[+] URL Detected : https://eyupergin.com/
[+] Title: Access Denied
[-] Internal Data Not Found

[+] URL Detected : https://eyupergin.com/blog/
[+] Title:  Access Denied
[-] Internal Data Not Found

```

<h3 align="left">Example 3 : Save </h2>

```
python3 WebScrapper.py  --save

Output;

Enter Dork : site:eyupergin.com
Scanning > site:eyupergin.com

[+] URL Detected : https://eyupergin.com/
[+] Title: Access Denied
[-] Internal Data Not Found

[+] URL Detected : https://eyupergin.com/blog/
[+] Title:  Access Denied
[-] Internal Data Not Found
^C

user@user:~$ cat site:eyupergin.com.txt
```

<h3 align="left">Example 4 : PDF </h2>

```
python3 WebScrapper.py

Output;

Enter Dork : site:github.com filetype:pdf
Scanning > site:github.com filetype:pdf

[+] URL Detected : http://vicziani.github.com/artifacts/asp_servlet.pdf
[-] Title: Title not found
[-] Internal Data Not Found

[+] URL Detected : https://www.github.com/cdrfiuba/programador/wiki/At89S8253_errata.pdf
[+] Title: AT89 Microcontrollers
[-] Internal Data Not Found

```

<h2 align="left">To-Do:</h2>

- [x]  Infrastructure Will Be Changed
- [x]  Modular Building Will Be Brought
- [x]  Arguments Will Be Replaced
- [ ] URL Scrapper

<h2 align="left">Developers:</h2>

[@EyupErgin](https://github.com/eyupergin)


