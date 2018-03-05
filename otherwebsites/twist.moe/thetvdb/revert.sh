toknow=$(cat temptoken.json | grep 'token' | cut -d "\"" -f4)

echo Changing 
echo $toknow
echo To
echo '#TOKEN#'

for i in $(ls -1 | grep 'js$')
do
	cat $i | sed "s/$toknow/#TOKEN#/g" > temp
	mv temp $i

done

