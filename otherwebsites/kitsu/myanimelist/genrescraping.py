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

conn = sqlite3.connect('anime.db')
c = conn.cursor()

c.execute("SELECT id FROM anime")
animelist = c.fetchall()

c.close()
conn.close()


#Create  a genremappings.db file
conn = sqlite3.connect('genremappings.db')
c = conn.cursor()

#Create table for the first time
c.execute("CREATE TABLE IF NOT EXISTS mappings (id INT, source_type BIT, genrelist TEXT)")
conn.commit()

#Anime
for mal_id in animelist:

    #Fetch from dab and if empty go ang scrape
    c.execute("SELECT * FROM mappings WHERE id = ?", [mal_id[0]])
    result = c.fetchone()

    if result != [] and result != "" and result != None:
        #no scraping
        print(result)
    else:
        
        curr_url = "https://myanimelist.net/anime/" + str(mal_id[0])
        print("curr_url",curr_url)

        soup_html = requests.get(curr_url).text
        htmlsoup = soup(soup_html , "html.parser")

        genretable = htmlsoup.find("table", {"width" : "100%"}).div

        genretable = genretable.findAll("div")

        for item in genretable:
            
            span = item.find("span")
            if span != None and span.text == "Genres:":
                
                genlist = []
                for genre in item.findAll("a"):
                    genlist.append(genre['title'])
                genlist = '|'.join(genlist)
                print(genlist)
                print('\n')

                c.execute("INSERT INTO mappings (id, source_type, genrelist) VALUES (?, ?, ?)",(mal_id[0], 0, genlist))
                conn.commit()
        
c.close()
conn.close()