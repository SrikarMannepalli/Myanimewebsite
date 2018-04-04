#TAKES MAL_ID AS AN ARGUMENT TO GET IMAGE AND DESCRIPTION

from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
import sqlite3, time , sys

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


mal_id = sys.argv[1]       #30276 for ONE PUNCH MAN

curr_url = "https://myanimelist.net/anime/" + str(mal_id)


uclient = ureq(curr_url)
soup_html = uclient.read()
uclient.close()
htmlsoup = soup(soup_html , "html.parser")


#print(str(htmlsoup.find("meta", {"property" : "og:url"})["content"].split("/")[5]))
print(str(htmlsoup.find("table", {"width" : "100%"}).div.div.a.img["src"]))
print(str(htmlsoup.find("span", {"itemprop":"description"}).text))
