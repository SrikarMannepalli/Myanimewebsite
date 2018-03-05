Date.prototype.getUnixTime = function() { return this.getTime()/1000|0 };
var c = new Date('#CUSTOMDATE#').getUnixTime();
console.log(c);
