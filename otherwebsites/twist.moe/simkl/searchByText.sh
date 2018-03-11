text=$1
#IF type is specified
if [ $# -eq 1 ]
then
	typ='anime'
else
	typ=$2
fi

url="https://api.simkl.com/search/$typ?q=$text&client_id=f62476556cc7cd5f05720424885a878c71df4f859cef9c15bbe9df862b608521"

wget -q -O h.json $url
cat h.json | python -m json.tool > outjson.json 
rm -f h.json
