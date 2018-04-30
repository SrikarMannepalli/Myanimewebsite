import requests
from bs4 import BeautifulSoup as soup
import sqlite3, time

mal = "https://myanimelist.net/"
topanimelist = "https://myanimelist.net/topanime.php?limit=14150"
#0 to 14250
topmangalist = "https://myanimelist.net/topmanga.php?limit=46100"
#0 to 46150
searchmal = "https://myanimelist.net/search/prefix.json?type=all&keyword=boku&v=1"
malanime = "https://myanimelist.net/search/prefix.json?type=anime&keyword=boku&v=1"
malmanga = "https://myanimelist.net/search/prefix.json?type=manga&keyword=boku&v=1"
malcharacter = "https://myanimelist.net/search/prefix.json?type=character&keyword=boku&v=1"
maluser = "https://myanimelist.net/search/prefix.json?type=user&keyword=boku&v=1"


#mal_id = 21 #ONE PIECE

conn = sqlite3.connect('myanimelist.db')
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS anime (id INT PRIMARY KEY, name TEXT, name_in_url TEXT, imglink TEXT)")
c.execute("CREATE TABLE IF NOT EXISTS manga (id INT PRIMARY KEY, name TEXT, name_in_url TEXT, imglink TEXT)")
c.execute("CREATE TABLE IF NOT EXISTS characters (id INT PRIMARY KEY, name TEXT, name_in_url TEXT, imglink TEXT)")
#c.execute("ALTER TABLE anime ADD name_in_url TEXT")

for i in range(0,14250,50): #UPTO 14250 is allowed
    curr_url = "https://myanimelist.net/topanime.php?limit=" + str(i)

    soup_html = requests.get(curr_url).text
    htmlsoup = soup(soup_html , "html.parser")

    div = htmlsoup.findAll("tr", {"class" : "ranking-list"})
    print("i :", i)
    for anime in div:
        an = anime.find("td",{"class":"title"})
        
        #The anime name
        name = an.findAll("a")[1].text

        url = an.a["href"]
        mal_id = url.split("/")


        curr_url2 = "https://myanimelist.net/anime/" + str(mal_id[4])
        print("curr_url2",curr_url2)

        soup_html2 = requests.get(curr_url2).text
        htmlsoup2 = soup(soup_html2 , "html.parser")


        #print(htmlsoup2.find("meta", {"property" : "og:url"})["content"].split("/")[5])
      #  print(htmlsoup2.find("table", {"width" : "100%"}).div.div.a.img["src"])

        try:
            image = htmlsoup2.find("table", {"width" : "100%"}).div.div.a.img["src"]
            print(image)
        except Exception:
            image = None

        #print("mal_id = ", mal_id[4], "name = ", mal_id[5])
        c.execute("SELECT * FROM anime WHERE id=?", [mal_id[4]])
        fetched = c.fetchall()
        print("Fetched from database", fetched)
        
        if fetched == []:
            c.execute("INSERT INTO anime (id, name, name_in_url, imglink) VALUES (?, ?, ?, ?)" , (mal_id[4], name, mal_id[5],image))
            #c.execute("UPDATE anime SET shortimg = ? WHERE id = ?" , (shortimg, mal_id[4]))        
            conn.commit()
            print('INSTERTED', url)

for i in range(0,46200,50): #UPTO 46150 is allowed
    curr_url = "https://myanimelist.net/topmanga.php?limit=" + str(i)
    print(curr_url)

    soup_html = requests.get(curr_url).text

    htmlsoup = soup(soup_html , "html.parser")

    div = htmlsoup.findAll("tr", {"class" : "ranking-list"})
    print("i :", i)
    for anime in div:
        an = anime.find("td",{"class":"title"})
        url = an.a["href"]
        name = an.findAll("a")[1].text
        mal_id = url.split("/")
        
        
        curr_url2 = "https://myanimelist.net/anime/" + str(mal_id[4])
        print("curr_url2",curr_url2)

        soup_html2 = requests.get(curr_url2).text
        htmlsoup2 = soup(soup_html2 , "html.parser")


        #print(htmlsoup2.find("meta", {"property" : "og:url"})["content"].split("/")[5])
      #  print(htmlsoup2.find("table", {"width" : "100%"}).div.div.a.img["src"])

        try:
            image = htmlsoup2.find("table", {"width" : "100%"}).div.div.a.img["src"]
            print(image)
        except Exception:
            image = None

        #print("mal_id = ", mal_id[4], "name = ", mal_id[5])
        c.execute("SELECT * FROM manga WHERE id=?", [mal_id[4]])
        fetched = c.fetchall()
        print("Fetched from database", fetched)
        
        if fetched == []:
            c.execute("INSERT INTO manga (id, name, name_in_url, imglink) VALUES (?, ?, ?, ?)" , (mal_id[4], name, mal_id[5],image))
            #c.execute("UPDATE manga SET shortimg = ? WHERE id = ?" , (shortimg, mal_id[4]))        
            conn.commit()
            print('INSTERTED', url)



c.close()
conn.close()