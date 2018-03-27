from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
import sqlite3, time

#conn = sqlite3.connect('thehyliadatabasesql.db')
#c = conn.cursor()


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

uclient = ureq(mal)
soup_html = uclient.read()
uclient.close()
htmlsoup = soup(soup_html , "html.parser")

print(str(htmlsoup.find("div",{"id":"menu"})))
