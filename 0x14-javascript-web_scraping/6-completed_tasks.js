#!/usr/bin/node

const request = require('request');
const dict = {};
const arg = process.argv;
request(arg[2], function (error, _response, body) {
  if (error) {
    console.error(error.message);
  }
  const jsonData = JSON.parse(body);
  for (let i = 0; i < jsonData.length; i++) {
    const id = jsonData[i].userId;
    const comp = jsonData[i].completed;
    if (comp && !dict[id]) {
      dict[id] = 0;
    }
    if (comp) ++dict[id];
  }
  console.log(dict);
});
