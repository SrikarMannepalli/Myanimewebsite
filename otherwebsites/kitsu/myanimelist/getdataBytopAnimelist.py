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

conn = sqlite3.connect('anime.db')
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS anime (id INT, name TEXT, description TEXT, imglink TEXT)")

for i in range(0,100,50): #UPTO 14150 is allowed
    curr_url = "https://myanimelist.net/topanime.php?limit=" + str(i)

    uclient = ureq(curr_url)
    soup_html = uclient.read()
    uclient.close()
    htmlsoup = soup(soup_html , "html.parser")

    div = htmlsoup.findAll("tr", {"class" : "ranking-list"})
    #print("i :", i)
    for anime in div:
        an = anime.find("td",{"class":"title"})
        url = an.a["href"]
        #print()
        mal_id = str(url).split("/")
        #print("mal_id = ", mal_id[4], "name = ", mal_id[5])
        c.execute("INSERT INTO anime (id, name) VALUES (?, ?)" , (mal_id[4],mal_id[5]))
        conn.commit()
        #print('\n')

c.execute("SELECT * FROM anime")
for row in c.fetchall():
    print(row)
