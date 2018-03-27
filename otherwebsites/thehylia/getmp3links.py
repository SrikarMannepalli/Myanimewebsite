#THIS FILE IS TO GENERATE A LOCAL DATA BASE FROM HTTPS://ANIME.THEHYLIA.COM
#ARGUMENT SHOULD BE A ALBUM_SONG_URL eg: https://anime.thehylia.com/soundtracks/album/hunter-x-hunter-2011-ed-single-just-awake/01%2520-%2520Just%2520Awake.mp3
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

thehylia = "https://anime.thehylia.com/"
music = "https://anime.thehylia.com/soundtracks/browse/all"
animusic = "https://anime.thehylia.com/downloads/browse/all"

import sys
program_name = sys.argv[0]
arguments = sys.argv[1:]
count = len(arguments)


for x in sys.argv[1:]:
    print(x)
    uclient = ureq(x)
    soup_html = uclient.read()
    uclient.close()
    htmlsoup = soup(soup_html , "html.parser")

    content = htmlsoup.find("table", {"class":"blog"})
    content = content.findAll("b")
        

    #with open('./database.db', 'w') as currfile:
    #    for link in content:
    #        currfile.write(str(link["href"]) + "||" + str(link.text) + "\n")
    print("ALBUM_URL||",str(content[0].a["href"]))
    print("ALBUM||",str(content[1].text))
    print("NAME||",str(content[2].text))
    print("URL||",str(content[3].a["href"]))

