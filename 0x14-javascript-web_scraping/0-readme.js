#!/usr/bin/node

const fs = require('fs');

const filename = process.argv;
fs.readFile(filename[2], 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
