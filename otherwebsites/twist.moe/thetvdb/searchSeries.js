var curl = require('curlconverter');

//searches can be made using 
//
//name
//imdbId
//zap2itId
//
//ONLY one of them
//
//eg
//
//(HERE I made all the requests but only one of them is needed)
//
//curl -X GET --header 'Accept: application/json' --header 'Accept-Language: en' --header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1MTk5OTg4MzgsImlkIjoiUm9vdHdvcmxkIiwib3JpZ19pYXQiOjE1MTk5MTI0MzgsInVzZXJpZCI6NDk5NzU2LCJ1c2VybmFtZSI6InBoYW5pcml0aHZpaiJ9.BGuk8oZ-fQEIIvKDNU7-hZp52cBPcpYYQ0P3WyYVNPGgx0DPsP7kfyQRgscYlccklcZPu6ONci0uh5Mkbb_kMlHzLymEWEnwQmKwtHbWdQ0rn_ZkZG9qePI8O0A22q-rtYlbRBAGOToHwi1C0lWXyBGRJo7Ti2HaagauOKc7kJYKH9aEkt_RsDrxNuv7qgQ_9ME0vA03VdMQFGQVTE2bu6KORUZl41UXf0TH1J13uC1peh_g_7jcPbs-CZ48LWTO1_flVaDEtkc1WZtffpavckAD46ppWEzfzGc5A7Jg28HvIgy2kcjPpyxD4J9jqLLALpMqxDRV4GFfGfTXf-wyKg' 'https://api.thetvdb.com/search/series?name=one%20piece&imdbId=t456345&zap2itId=634y'
//

var curlinput = "curl -X GET --header 'Accept: application/json' --header 'Accept-Language: en' --header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1MjAzMzMzOTQsImlkIjoiUm9vdHdvcmxkIiwib3JpZ19pYXQiOjE1MjAyNDY5OTQsInVzZXJpZCI6NDk5NzU2LCJ1c2VybmFtZSI6InBoYW5pcml0aHZpaiJ9.hfV1z659hdF2EGtUSMYvksZfOwxz7emG6Q3B_WtDQZwyBsLN9DnffLCUxPEfTSiSwaB1oitiWM6RxprfojHpsiJnUwqNDh5D93gPvMJZookmT_d9yrWNcm1gF5uDo9-ow95qA0XeoZk_D7h4KnjsrIYOC11NmzQmzQATeQlENfkUu_d0B1CuJyuy2dOu4CmHU_gHjiiKoXDB7xUGHfp1isgJmJMjBUfyRcIaeKa6hwYsGC9Z55WLy_QNMW10mryvZQcwS8nje3yOGSJt-DIOhielC8vavfHw5kPZzHT_s5CWYgDoLRApS-n9ch7zWGGmX2Q8wwqawviLoLwK_APalg' 'https://api.thetvdb.com/search/series?name=one%20piece'";

var e = curl.toNode(curlinput);
console.log(e);
