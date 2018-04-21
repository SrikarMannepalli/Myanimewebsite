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


conn = sqlite3.connect('characters.db')
conn.text_factory = str
c = conn.cursor()

c.execute("SELECT id FROM characters")
characters_list = c.fetchall()

for id in characters_list:
    
    c.execute("SELECT imglink, description FROM characters WHERE id = ?", [id[0]])
    out = c.fetchone()
	
    if out[0] != None and out[0] != "" and out[1] != None and out[1] != "":
        print(id[0])
    else:
        curr_url = "https://myanimelist.net/character/" + str(id[0])
        print("curr_url",curr_url)

        soup_html = requests.get(curr_url).text
        htmlsoup = soup(soup_html , "html.parser")


        #print(str(htmlsoup.find("meta", {"property" : "og:url"})["content"].split("/")[5]))
        info_table = htmlsoup.find("table", {"width" : "100%"})
        mappings_table = htmlsoup.find("table", {"width" : "100%"}).td
        desc_page = info_table.find("td",{"style":"padding-left: 5px;"})

        try:
            image = str(mappings_table.div.a.img["src"])
        except Exception:
            image = None

        animeography = mappings_table.findAll("table")[0]
        mangaography = mappings_table.findAll("table")[1]
        
        for anime_mapping in animeography.findAll("div",{"class":"picSurround"}):
            try:
                print("anime id",anime_mapping.a['href'].split('/')[-2])
            except Exception:
                print("animeography not found")
        
        for manga_mapping in mangaography.findAll("div",{"class":"picSurround"}):
            try:
                print("manga id",manga_mapping.a['href'].split('/')[-2])
            except Exception:
                print("mangaography not found")
        
    
        #Remove all the other divs and get only the character's details
        try:
            desc_page.find("div",{"id":"horiznav_nav"}).decompose()
            desc_page.find("div",{"class":"breadcrumb"}).decompose()
        except Exception:
            print("error in removing nav bar or breadcrumb")

        try:
            for el in desc_page.findAll("table",{"width":"100%"}):
                el.decompose()
        except Exception:
            print("error in removing voice actor tables")
        
        try:
            desc_page.find("h2").decompose()
        except Exception:
            print("error in removing feautred articles heading")
        
        try:    
            desc_page.find("div",{"class":"detail-page-featured-article"}).decompose()
        except Exception:
            print("error in removing featured-articles div")
        
        try:
            desc_page.find("div",{"class":"mauto"}).decompose()
        except Exception:
            print("error in removing mauto ads div I guess")

        try:
            for el in desc_page.findAll("div",{"class":"normal_header"}):
                if el.text == "Voice Actors":
                    el.decompose()
        except Exception:
            print("error in removing voice actors heading")

        #Grab japanesename and english names
        try:
            japanese_name = desc_page.find("div",{"class":"normal_header"}).span.small.text
            desc_page.find("div",{"class":"normal_header"}).span.decompose()
            english_name = desc_page.find("div",{"class":"normal_header"}).text
            if english_name != None and english_name != "":
                desc_page.find("div",{"class":"normal_header"}).decompose()
        except Exception:
            japanese_name = None
            english_name = None
            print("japanese or eng name failed")

        print(japanese_name,english_name)
        desc = desc_page.encode_contents()
        c.execute("UPDATE characters SET imglink = ? , description = ? WHERE id = ?", (image , desc, id[0]))
        conn.commit()
        print(image, desc)


c.close()
conn.close()