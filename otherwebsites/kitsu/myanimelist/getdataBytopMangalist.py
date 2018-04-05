from urllib.request import urlopen as ureq
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


#mal_id = 21 #ONE PIECE

conn = sqlite3.connect('manga.db')
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS manga (id INT PRIMARY KEY, name TEXT, description TEXT, imglink TEXT, shortimg TEXT)")
#c.execute("ALTER TABLE manga ADD shortimg TEXT")

for i in range(0,100,50): #UPTO 46100 is allowed
    curr_url = "https://myanimelist.net/topmanga.php?limit=" + str(i)

    uclient = ureq(curr_url)
    soup_html = uclient.read()
    uclient.close()
    htmlsoup = soup(soup_html , "html.parser")

    div = htmlsoup.findAll("tr", {"class" : "ranking-list"})
    #print("i :", i)
    for anime in div:
        an = anime.find("td",{"class":"title"})
        url = an.a["href"]
        #print(str(an.a.img['data-src']))
        shortimg = str(an.a.img['data-src'])
        print(shortimg)
        mal_id = str(url).split("/")
        #print("mal_id = ", mal_id[4], "name = ", mal_id[5])
        c.execute("INSERT INTO manga (id, name, shortimg) VALUES (?, ?, ?)" , (mal_id[4], mal_id[5], shortimg))
        #c.execute("UPDATE anime SET shortimg = ? WHERE id = ?" , (shortimg, mal_id[4]))        
        conn.commit()
        #print('\n')

c.execute("SELECT * FROM manga")
for row in c.fetchall():
    print(row)

c.close()
conn.close()
