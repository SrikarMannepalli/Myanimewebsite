import requests
from bs4 import BeautifulSoup as soup
import sqlite3, time

mal = "https://myanimelist.net/"
topanimelist = "https://myanimelist.net/topanime.php?limit=14150"
#0 to 14150
topmangalist = "https://myanimelist.net/topmanga.php?limit=46100"
#0 to 46100
searchmal = "https://myanimelist.net/search/prefix.json?type=all&keyword=boku&v=1"
malanime = "https://myanimelist.net/search/prefix.json?type=anime&keyword=boku&v=1"
malmanga = "https://myanimelist.net/search/prefix.json?type=manga&keyword=boku&v=1"
malcharacter = "https://myanimelist.net/search/prefix.json?type=character&keyword=boku&v=1"
maluser = "https://myanimelist.net/search/prefix.json?type=user&keyword=boku&v=1"


#Connect to anime.db and get all the ids present in it
conn = sqlite3.connect('anime.db')
c = conn.cursor()

c.execute("SELECT id FROM anime")

animelist = c.fetchall()

c.close()
conn.close()

#Connect to characters.db and add shortimg, id , name, name_in_url

conn = sqlite3.connect('characters.db')
c = conn.cursor()

for mal_id in animelist:
    
    pass

c.close()

conn.close()
