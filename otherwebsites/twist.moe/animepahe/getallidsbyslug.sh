#OUTPUTS THE IDS AND THUMBNAILS in a array of objects named slug
#INPUT CAN BE SLUG OR ID


#If input is a number it is a id
if [[ $1 =~ ^-?[0-9]+$ ]]
then	
anid=$1
slug=$(./slug.sh $anid)

else
#Else it is a slug

slug=$1
anid=$(./id.sh $slug)
fi

#page = 1
page=1

link=$(echo https://animepahe.com/api?m=release\&id=$anid\&l=30\&sort=episode_asc\&page=$page)
#echo LINK $link
currpage=0
lastpage=1 #something thats not currpage
totids=0
while [[ $currpage != $lastpage ]]
do
#echo ${id[*]}
link=$(echo https://animepahe.com/api?m=release\&id=$anid\&l=30\&sort=episode_asc\&page=$page)
#echo LINK $link
wget -q -O page.json $link
echo var data = $(cat page.json) > dpage.json
cat dpage.json getbashcode.txt > dpage.js
node dpage.js > temp.sh
. temp.sh
#cat temp.sh
#echo ${id[*]}
#echo from $start to $end
#echo currpage $currpage / lastpage $lastpage
page=$((currpage+1))
#echo page $page
done
x=0
rm -f out.json
#echo ${id[*]}
oid=$(echo $anid)
var=$(echo $slug | tr '-' '_')
echo "var $var = ["
echo "var $var = [" > out$oid.json
for i in ${thumb[*]}
do
	x=$((x+1))
	thumbnomd[$x]=$(echo $i | sed 's/\.md\.jpg$/\.jpg/')
done
x=0
for i in ${id[*]}
do
	x=$((x+1))
	echo '{'
	echo '{' >> out$oid.json
	echo \"id\":$i ,
	echo \"id\":$i , >> out$oid.json
       	echo \"thumb\":\"${thumbnomd[$x]}\"
       	echo \"thumb\":\"${thumbnomd[$x]}\" >> out$oid.json
	if [[ $totids != $x ]]
	then
	echo '},'
	echo '},' >> out$oid.json
	else
	echo '}'
	echo '}' >> out$oid.json
	fi
done
echo ']'
echo ']' >> out$oid.json
