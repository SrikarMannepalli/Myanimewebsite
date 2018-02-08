for i in $(ls -1 -v | grep -E 'mp4$|mkv$|ogg$|avi$|gif$')
do
	j=$(echo $i | tr " " "_")
	echo mv $i $j
done
