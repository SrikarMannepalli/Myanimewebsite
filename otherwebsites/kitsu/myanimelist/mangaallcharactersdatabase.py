

#To create a database called mangacharacters.db which contains all characters from a particular manga 

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


#Connect to manga.db and get all the ids present in it
conn = sqlite3.connect('manga.db')
c = conn.cursor()

c.execute("SELECT id, name_in_url FROM manga")

mangalist = c.fetchall()

c.close()
conn.close()

#Connect to mangacharacters.db and add shortimg, id , name, name_in_url

conn = sqlite3.connect('mangacharacters.db')
c = conn.cursor()
#Create table for the first time
c.execute("CREATE TABLE IF NOT EXISTS mappings (manga_id INT, character_id INT)")
conn.commit()

for item in mangalist:


    #If some ids alrady exists with his manga id

    #Insert into mappings if not found
    c.execute("SELECT * FROM mappings WHERE manga_id = ?", (item[0],))
    exists = c.fetchall()


    if exists != None and exists != "" and exists != []:
        print("it exists")
        print(exists)
    else:

        curr_url = "https://myanimelist.net/manga/" + str(item[0]) + "/" + item[1] + "/characters"
        print(curr_url)

        soup_html = requests.get(curr_url).text
        htmlsoup = soup(soup_html, "html.parser")

        content = htmlsoup.find("div", {"id":"content"})

        #manga div below the main image
        details = content.find("div", {"class":"js-scrollfix-bottom"})
        #print(details)
        #Characters div
        content = content.find("div", {"class":"js-scrollfix-bottom-rel"})

        characters = content.findAll("table", recursive=False)
        for character in characters:
            link = character.findAll("td", {"valign":"top"})[1]
            url = link.a['href']
            id = url.split('/')[-2]
            dtype = url.split('/')[-3]
            if dtype == "character":
                print(id)
                #print(name_in_url)
                #print(role)
                
                #Insert into mappings if not found
                c.execute("SELECT * FROM mappings WHERE manga_id = ? AND character_id = ?", (item[0], id))
                exists = c.fetchone()

                if exists != None and exists != "" and exists != []:
                    print("it exists " + id)
                else:        
                    c.execute("INSERT INTO mappings (manga_id, character_id) VALUES (?, ?)", (item[0], id))
                    conn.commit()
                    print(str(id) + " INSERTED FOR " + str(item[0]))
            elif dtype == "people":
                print("Staff I Guess")
            else:
                print("H>>>>>M")
        
            
            
        


c.close()
conn.close()
