out=$(node $1 | node)

if [[ $1 == "login.js" || $1 == "refreshtoken.js" ]]
then
	echo $out > temptoken.json
	echo $out
fi
