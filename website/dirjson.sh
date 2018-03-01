IFS=$'\n'
j=0
for i in $(ls -1 -v)
do
if [ -d $i ]
then
j=$((j+1))
fi
done
c=0
echo "{" > tot.json
for i in $(ls -1 -v)
do
if [ -d $i ]
then
c=$((c+1))
tot=$(ls -1 -v $i | grep -E 'jpg$|png$|jpeg$|$gif' | wc -l)
exten=$(ls -1 -v $i | grep -E 'jpg$|png$|jpeg$|$gif' | rev | cut -d "." -f1| rev | sort -u)
name=$(ls -1 -v $i | grep -E 'jpg$|png$|jpeg$|$gif' | sed 's/[0-9]*\./\./g' | sort -u | cut -d "." -f1)
echo -e "{\"tot\":$tot,\"name\":\"$name\",\"exten\":\"$exten\"}"
echo -e "\t $i : {\n\t\"tot\":$tot,\n\t\"name\":\"$name\",\n\t\"exten\":\"$exten\"\n\t}" >> tot.json
if [ $j -ne $c ]
then    
echo -e "\t,\n" >> tot.json
fi
fi
done
echo "}" >> tot.json

