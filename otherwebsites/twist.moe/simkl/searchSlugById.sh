#INPUT simkl_id

#OUTPUT SLUG

#Eg.
#	searchSlugById.sh 38636
#	one-piece

simklid=$1


wget -q -O slug.json "https://api.simkl.com/search/id?simkl=$simklid&client_id=f62476556cc7cd5f05720424885a878c71df4f859cef9c15bbe9df862b608521"

cat slug.json | sed 's/}/\n/g' | sed 's/,/\n/g' | sed 's/{/\n/g' | sed 's/\[/\n/g' | sed 's/\]/\n/g' | sed '/^$/d' | grep 'slug' | cut -d ":" -f2 | cut -d "\"" -f2
