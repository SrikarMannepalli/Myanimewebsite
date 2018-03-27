//base64 to jpeg or png

var fs = require('fs');

var x;
var data = fs.readFileSync("./ex.txt",'utf8');

x = data
console.log(x)
var data = x.replace(/^data:image\/\w+;base64,/, "");
var s = new Buffer(data, 'base64')

fs.writeFile('./hmm.jpeg', s)
