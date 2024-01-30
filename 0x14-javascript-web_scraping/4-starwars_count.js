#!/usr/bin/node

const request = require('request');

const arg = process.argv;
let c = 0;
request(arg[2], function (error, _response, body) {
  if (error) {
    console.error(error.message);
  }
  const jsonData = JSON.parse(body);
  for (let i = 0; i < jsonData.results.length; i++) {
    for (let j = 0; j < jsonData.results[i].characters.length; j++) {
      if (jsonData.results[i].characters[j].includes('18')) {
        c++;
      }
    }
  }
  console.log(c);
});
