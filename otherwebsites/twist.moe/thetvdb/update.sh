token=$(cat temptoken.json | grep "token" | cut -d "\"" -f4)
echo token now $token

for i in $(ls -1 | grep 'js$')
do
	echo FILE $i
	cat $i | sed "s/#TOKEN#/$token/g" > temp
	mv temp $i

done
