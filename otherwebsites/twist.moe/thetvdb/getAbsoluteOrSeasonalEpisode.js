var curl = require('curlconverter');

//absoluteNumber is enough
//
//airedSeason will list all of that season's episodes
//
//page=1 can be used
//
//if this url is used
//
//the episode number is relative to the particular season
//
//https://api.thetvdb.com/series/81797/episodes/query?airedSeason=3&airedEpisode=1
//
//
//IMDB ID CAN ALSO BE USED
//
//https://api.thetvdb.com/series/81797/episodes/query?airedSeason=3&airedEpisode=1&imdbId=333333


var curlinput = "curl -X GET --header 'Accept: application/json' --header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1MjAzMzMzOTQsImlkIjoiUm9vdHdvcmxkIiwib3JpZ19pYXQiOjE1MjAyNDY5OTQsInVzZXJpZCI6NDk5NzU2LCJ1c2VybmFtZSI6InBoYW5pcml0aHZpaiJ9.hfV1z659hdF2EGtUSMYvksZfOwxz7emG6Q3B_WtDQZwyBsLN9DnffLCUxPEfTSiSwaB1oitiWM6RxprfojHpsiJnUwqNDh5D93gPvMJZookmT_d9yrWNcm1gF5uDo9-ow95qA0XeoZk_D7h4KnjsrIYOC11NmzQmzQATeQlENfkUu_d0B1CuJyuy2dOu4CmHU_gHjiiKoXDB7xUGHfp1isgJmJMjBUfyRcIaeKa6hwYsGC9Z55WLy_QNMW10mryvZQcwS8nje3yOGSJt-DIOhielC8vavfHw5kPZzHT_s5CWYgDoLRApS-n9ch7zWGGmX2Q8wwqawviLoLwK_APalg' 'https://api.thetvdb.com/series/81797/episodes/query?absoluteNumber=42&airedSeason=3'";

var e = curl.toNode(curlinput);
console.log(e);
