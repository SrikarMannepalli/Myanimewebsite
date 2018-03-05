var curl = require('curlconverter');

//here in the link
//
//
//https://api.thetvdb.com/series/81797/filter?keys=status%2Cgenre%2CairsDayOfWeek%2CimdbId%2CairsTime%2Crating%2CsiteRatingCount%2CfirstAired%2Cnetwork%2Cruntime%2Coverview%2ClastUpdated%2Cadded%2CaddedBy%2Cid%2CseriesName%2Caliases%2CnetworkId%2Cbanner%2CseriesId%2Czap2itId%2CsiteRating
//
//
//only one or more of the filters can be used
//
//eg
//
//
//https://api.thetvdb.com/series/81797/filter?keys=status%2Cgenre
//
//

var curlinput = "curl -X GET --header 'Accept: application/json' --header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1MjAzMzMzOTQsImlkIjoiUm9vdHdvcmxkIiwib3JpZ19pYXQiOjE1MjAyNDY5OTQsInVzZXJpZCI6NDk5NzU2LCJ1c2VybmFtZSI6InBoYW5pcml0aHZpaiJ9.hfV1z659hdF2EGtUSMYvksZfOwxz7emG6Q3B_WtDQZwyBsLN9DnffLCUxPEfTSiSwaB1oitiWM6RxprfojHpsiJnUwqNDh5D93gPvMJZookmT_d9yrWNcm1gF5uDo9-ow95qA0XeoZk_D7h4KnjsrIYOC11NmzQmzQATeQlENfkUu_d0B1CuJyuy2dOu4CmHU_gHjiiKoXDB7xUGHfp1isgJmJMjBUfyRcIaeKa6hwYsGC9Z55WLy_QNMW10mryvZQcwS8nje3yOGSJt-DIOhielC8vavfHw5kPZzHT_s5CWYgDoLRApS-n9ch7zWGGmX2Q8wwqawviLoLwK_APalg' 'https://api.thetvdb.com/series/81797/filter?keys=status%2Cgenre%2CairsDayOfWeek%2CimdbId%2CairsTime%2Crating%2CsiteRatingCount%2CfirstAired%2Cnetwork%2Cruntime%2Coverview%2ClastUpdated%2Cadded%2CaddedBy%2Cid%2CseriesName%2Caliases%2CnetworkId%2Cbanner%2CseriesId%2Czap2itId%2CsiteRating";

var e = curl.toNode(curlinput);
console.log(e);
