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
echo "{" 
for i in $(ls -1 -v)
do
if [ -d $i ]
then
c=$((c+1))
tot=$(ls -1 -v $i | grep -E 'jpg$|png$|jpeg$|$gif' | wc -l)
exten=$(ls -1 -v $i | grep -E 'jpg$|png$|jpeg$|$gif' | rev | cut -d "." -f1| rev|sort -u)
name=$(ls -1 -v $i | grep -E 'jpg$|png$|jpeg$|$gif')
s=$(echo  "sed 's/[0-9]*\.$exten\$/\.$exten/g'")
v=$( echo $name | sed 's/ $/\n/g' | eval $s | sort -u | cut -d "." -f1)
echo -e "\t $i : {\n\t\"tot\":$tot,\n\t\"name\":\"$v\",\n\t\"exten\":\"$exten\"\n\t}"
echo -e "\t $i : {\n\t\"tot\":$tot,\n\t\"name\":\"$v\",\n\t\"exten\":\"$exten\"\n\t}" >> tot.json
if [ $j -ne $c ]
then
echo -e "\t,\n" >> tot.json
echo -e "\t,\n"
fi
fi
done
echo "}" >> tot.json
echo "}"
