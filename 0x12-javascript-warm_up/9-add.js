#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const sum = add(+process.argv[2], +process.argv[3]);
console.log(sum);
