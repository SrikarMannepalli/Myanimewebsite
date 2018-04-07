#THIS FILE IS TO GENERATE A LOCAL DATA BASE FROM HTTPS://ANIMEPAHE.COM
#Argument id NEEDED

#from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
import sqlite3, time, sys
import json
import requests

#curl  -s https://animepahe.com/anime/$slug | grep 'getJSON' | cut -d "'" -f2 | cut -d "&" -f2 | cut -d "=" -f2


anime = "https://animepahe.com/anime/"

id = 4 #one-piece

api = 'https://animepahe.com/api?m=release&id=' + str(id) + '&l=2&sort=episode_asc&page=' + '1'

nexturl = "nothing really"

#curr_url = anime + slug 
while nexturl != None:
    print("url", api)
    #COnnect to db
    conn = sqlite3.connect('pahe.db')
    c = conn.cursor()

    respie = requests.get(api)
    #print(respie.text)

    htmlsoup = soup(respie.text , "html.parser")



    data = json.loads(str(htmlsoup))

    nexturl = data['next_page_url']
    api = nexturl + '&m=release&l=30&sort=episode_asc&id=' + str(id)

    for item in data['data']:

        #print(item)
        print("title",item['title'])
        print("snapshot",item['snapshot'])
        print("filler",item['filler'])
        print("slug",item['anime_slug'])
        print("created_at",item['created_at'])
        print("id",item['id'])

c.close()
conn.close()
