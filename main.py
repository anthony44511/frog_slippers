from bs4 import BeautifulSoup as bs
import requests
import os
os.system("cls")


url = "https://secure.runescape.com/m=itemdb_oldschool/Frog+slippers/viewitem?obj=23288"
html = requests.get(url)

s = bs(html.content, "html.parser")


result = s.find(class_='stats')


if result:
    print(result.find('span')['title'])