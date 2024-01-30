#!/usr/bin/node

const request = require('request');

const arg = process.argv;
request(arg[2], function (error, response) {
  if (error) {
    console.error(error.message);
  }
  console.log('code:', response && response.statusCode);
});
