#THIS FILE IS TO GENERATE A LOCAL DATA BASE FROM HTTPS://ANIME.THEHYLIA.COM
#NO ARGUMENTS NEEDED

from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
import sqlite3, time

conn = sqlite3.connect('thehyliadatabasesql.db')
c = conn.cursor()


thehylia = "https://anime.thehylia.com/"
music = "https://anime.thehylia.com/soundtracks/browse/all"
animusic = "https://anime.thehylia.com/downloads/browse/all"

#Music first

uclient = ureq(music)
soup_html = uclient.read()
uclient.close()
htmlsoup = soup(soup_html , "html.parser")

content = htmlsoup.find("table", {"class":"blog"})
content = content.find("p", {"align":"left"})
content = content.findAll("a")

c.execute("CREATE TABLE IF NOT EXISTS albums (album_id INT, url TEXT, name TEXT, unix INT)")

album_id = 0

for link in content:
    unix = time.time()
    global album_id
    album_id += 1
    url = str(link["href"])
    name = str(link.text)

    c.execute("INSERT INTO albums (album_id, url, name, unix) VALUES (?, ?, ?, ?)",
            (album_id, url, name, unix))
    conn.commit()

#c.execute("SELECT * FROM albums")
#for row in c.fetchall():
#    print(row)


c.close()
conn.close()
