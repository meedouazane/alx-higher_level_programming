#!/usr/bin/node

const request = require('request');

const arg = process.argv;
const url = 'https://swapi-api.alx-tools.com/api/films/'.concat(arg[2]);
request(url, function (error, _response, body) {
  if (error) {
    console.error(error.message);
  }
  const jsonData = JSON.parse(body);
  for (let i = 0; i < jsonData.characters.length; i++) {
    request(jsonData.characters[i], function (_error, _response, body) {
      const jsonName = JSON.parse(body);
      console.log(jsonName.name);
    });
  }
});
