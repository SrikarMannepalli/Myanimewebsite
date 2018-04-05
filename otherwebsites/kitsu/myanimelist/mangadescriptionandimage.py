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

conn = sqlite3.connect('manga.db')
c = conn.cursor()

c.execute("SELECT id FROM manga")

for mal_id in c.fetchall():
    
    c.execute("SELECT imglink, description FROM manga WHERE id = ?", [mal_id[0]])
    out = c.fetchone()
	
    if out[0] != None and out[1] != None:
        print(mal_id[0])
    else:    
        curr_url = "https://myanimelist.net/manga/" + str(mal_id[0])
        print("curr_url",curr_url)

        uclient = ureq(curr_url)
        soup_html = uclient.read()
        uclient.close()
        htmlsoup = soup(soup_html , "html.parser")


        #print(str(htmlsoup.find("meta", {"property" : "og:url"})["content"].split("/")[5]))
        print(str(htmlsoup.find("table", {"width" : "100%"}).div.div.a.img["src"]))
        #print(str(htmlsoup.find("span", {"itemprop":"description"}).text))
        try:
            image = str(htmlsoup.find("table", {"width" : "100%"}).div.div.a.img["src"])
        except Exception:
            image = None
        try:
            desc = str(htmlsoup.find("span", {"itemprop":"description"}).text)
        except Exception:
            desc = None

        c.execute("UPDATE manga SET imglink = ? , description = ? WHERE id = ?", (image , desc , mal_id[0]))
        conn.commit()
