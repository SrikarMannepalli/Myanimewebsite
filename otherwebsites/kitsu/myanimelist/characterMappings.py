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

# Connect to characters.db
# IMPORTANT Characters are not different from anime and manga 
# Need to scarpe 
# Image from https://myanimelist.net/character/40/ eg. https://myanimelist.cdn-dena.com/images/characters/9/310307.jpg
# smallimage from https://myanimelist.net/anime/21   eg. https://myanimelist.cdn-dena.com/r/23x32/images/characters/9/310307.webp?s=2a09d6b2a4761d0fafd6d05b9894bc46
# Allimages from https://myanimelist.net/character/40/Luffy_Monkey_D/pictures 
# Description from https://myanimelist.net/character/40/
# Animeography and Mangaography from https://myanimelist.net/character/40/


#Get the characters list from the characters.db
conn = sqlite3.connect('characters.db')
conn.text_factory = str
c = conn.cursor()

c.execute("SELECT id FROM characters")
characters_list = c.fetchall()


c.close()
conn.close()


#Connect to charactersmappings.db
conn = sqlite3.connect('charactermappings.db')
conn.text_factory = str
c = conn.cursor()


#CREATE A TABLE FOR THE FIRST TIME

c.execute("CREATE TABLE IF NOT EXISTS characters (character_id INT, source_type BIT, source_id INT)")
conn.commit()


for id in characters_list:
    
    c.execute("SELECT source_id FROM characters WHERE character_id = ?", [id[0]])
    out = c.fetchone()
	
    if out:
        print(out[0],id)
    else:
        curr_url = "https://myanimelist.net/character/" + str(id[0])
        print("curr_url",curr_url)

        soup_html = requests.get(curr_url).text
        htmlsoup = soup(soup_html , "html.parser")


        #print(str(htmlsoup.find("meta", {"property" : "og:url"})["content"].split("/")[5]))
        info_table = htmlsoup.find("table", {"width" : "100%"})
        mappings_table = htmlsoup.find("table", {"width" : "100%"}).td
        desc_page = info_table.find("td",{"style":"padding-left: 5px;"})

        animeography = mappings_table.findAll("table")[0]
        mangaography = mappings_table.findAll("table")[1]
        
        for anime_mapping in animeography.findAll("div",{"class":"picSurround"}):
            try:
                print("anime id",anime_mapping.a['href'].split('/')[-2])
                anime_id = anime_mapping.a['href'].split('/')[-2]
                c.execute("INSERT INTO characters VALUES (?, ?, ?)",(id[0], 0, anime_id))
                conn.commit()
                print("inserted anime",anime_id)
            except Exception as e:
                print("animeography not found",e)
        
        for manga_mapping in mangaography.findAll("div",{"class":"picSurround"}):
            try:
                print("manga id",manga_mapping.a['href'].split('/')[-2])
                manga_id = manga_mapping.a['href'].split('/')[-2]
                c.execute("INSERT INTO characters VALUES (?, ?, ?)",(id[0], 1, manga_id))
                conn.commit()
                print("inserted manga",manga_id)
            except Exception as e:
                print("mangaography not found",e)
        
    

c.close()
conn.close()