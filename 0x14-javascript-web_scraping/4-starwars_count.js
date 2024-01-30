#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/';
const wedge = 'https://swapi-api.alx-tools.com/api/people/18/';
let c = 0;
request(url, function (error, _response, body) {
  if (error) {
    console.error(error.message);
  }
  const jsonData = JSON.parse(body);
  for (let i = 0; i < jsonData.results.length; i++) {
    for (let j = 0; j < jsonData.results[i].characters.length; j++) {
      if (jsonData.results[i].characters[j] === wedge) {
        c++;
      }
    }
  }
  console.log(c);
});
