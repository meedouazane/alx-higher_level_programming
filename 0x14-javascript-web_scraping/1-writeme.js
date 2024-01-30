#!/usr/bin/node

const fs = require('fs');

const arg = process.argv;
fs.writeFile(arg[2], arg[3], 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
