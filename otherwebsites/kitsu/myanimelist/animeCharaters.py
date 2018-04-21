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

c.execute("SELECT id, name_in_url FROM anime")

animelist = c.fetchall()

c.close()
conn.close()

#Connect to characters.db and add shortimg, id , name, name_in_url

conn = sqlite3.connect('characters.db')
c = conn.cursor()
#Create table for the first time
c.execute("CREATE TABLE IF NOT EXISTS characters (id INT, name TEXT, description TEXT, name_in_url TEXT, imglink TEXT, shortimg TEXT, role TEXT, fav_count INT)")
conn.commit()

for item in animelist:
    curr_url = "https://myanimelist.net/anime/" + str(item[0]) + "/" + item[1] + "/characters"
    print(curr_url)

    soup_html = requests.get(curr_url).text
    htmlsoup = soup(soup_html, "html.parser")

    content = htmlsoup.find("div", {"id":"content"})

    #Anime div below the main image
    details = content.find("div", {"class":"js-scrollfix-bottom"})
    #print(details)
    #Characters div
    content = content.find("div", {"class":"js-scrollfix-bottom-rel"})

    characters = content.findAll("table", recursive=False)
    for character in characters:
        shortimg = character.find("td", {"valign":"top"})
        shortimg = shortimg.img['data-src']
        link = character.findAll("td", {"valign":"top"})[1]
        url = link.a['href']
        name = link.a.text
        name_in_url = url.split('/')[-1]
        id = url.split('/')[-2]
        role = link.small.text
        #if this is character
        dtype = url.split('/')[-3]
        if dtype == "character":
            print(name)
            #print(id)
            #print(name_in_url)
            #print(role)
            
            #Insert into characters if not found
            c.execute("SELECT name FROM characters WHERE id = ?", [id])
            exists = c.fetchone()
            if exists != None and exists != "":
                print("it exists " + id)
            else:        
                c.execute("INSERT INTO characters (id, name, name_in_url, shortimg, role) VALUES (?, ?, ?, ?, ?)", (id, name, name_in_url, shortimg, role))
                conn.commit()
                print(name + " INSERTED")
        elif dtype == "people":
            print("Staff I Guess")
        else:
            print("H>>>>>M")
    
        
        
    


c.close()
conn.close()
