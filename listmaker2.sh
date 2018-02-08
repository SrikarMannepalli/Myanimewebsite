#It will create a directory listing of videos
tot=$(ls -1 -v | grep -E 'mp4$|mkv$|ogg$|avi$|gif$' | wc -l)
if [ -f vlist.txt ]
then 
	rm vlist.txt
fi
for i in $(ls -1 -v | grep -E 'mp4$|mkv$|ogg$|avi$|gif$')
do
	j=$(echo $i | tr " " "_")
	echo mv $i $j
	echo $j >> vlist.txt
done
echo "{\"totaleps\":$tot}" > tot.json
#PWD inside folder with ordered animevideos
