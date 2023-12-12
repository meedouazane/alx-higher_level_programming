#!/usr/bin/node
const fs = require('fs');
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];
const data1 = fs.readFileSync(fileA).toString();
const data2 = fs.readFileSync(fileB).toString();
const data = data1 + data2;
fs.writeFileSync(fileC, data);
