#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const arg = process.argv;
request(arg[2], function (error, _response, body) {
  if (error) {
    console.error(error.message);
  }
  fs.writeFile(arg[3], body, 'utf8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
