#!/usr/bin/node
const list = require('./100-data.js').list;
console.log(list);
let i = -1;
const mult = list.map((x) => {
  i++;
  return x * i;
});
console.log(mult);
