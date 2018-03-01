#PWD inside folder with ordered animevideos
#This stores names of videos in a list named 
#vlist.txt
#and a json file with number of videos in it
if [ -f vlist.txt ]
then 
	rm vlist.txt
fi
v=0
for i in $(ls -1 -v | grep -E 'mp4$|mkv$|ogg$|avi$|gif$')
do
	j=$(echo $i | tr " " "_")
	echo mv $i $j
	echo $j >> vlist.txt
	v=$((v+1))
done
echo "{\"total\" : $v}" > list.json
