var request = require('request');

request('https://api.simkl.com/search/${type}?q=${query}&client_id=${client_id}', function (error, response, body) {
  console.log('Status:', response.statusCode);
  console.log('Headers:', JSON.stringify(response.headers));
  console.log('Response:', body);
});
