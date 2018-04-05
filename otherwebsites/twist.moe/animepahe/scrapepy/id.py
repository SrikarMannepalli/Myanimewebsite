#THIS FILE IS TO GENERATE A LOCAL DATA BASE FROM HTTPS://ANIMEPAHE.COM
#Argument ID NEEDED

#from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
import sqlite3, time, sys
import json
import requests

#curl  -s https://animepahe.com/anime/$slug | grep 'getJSON' | cut -d "'" -f2 | cut -d "&" -f2 | cut -d "=" -f2


anime = "https://animepahe.com/anime/"

slug = "one-piece" #SLUG generally available from scraping https://animepahe.com/anime


curr_url = anime + slug 

print("url", curr_url)
#COnnect to db
conn = sqlite3.connect('pahe.db')
c = conn.cursor()

#try:
#	uclient = ureq(curr_url)
#	soup_html = uclient.read()
#	uclient.close()
#except Exception:

respie = requests.get(curr_url)
#print(respie.text)

htmlsoup = soup(respie.text , "html.parser")


poster = htmlsoup.find("div", {"class" : "anime-poster"}).a['href']
desc = htmlsoup.find("div", {"class":"anime-synopsis"})

#data = json.loads(str(htmlsoup))

print(str(poster))
print(str(desc.text))

c.close()
conn.close()
