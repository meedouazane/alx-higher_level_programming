#!/usr/bin/node
const array = [];
if (process.argv.length <= 3) {
  console.log('0');
  process.exit(1);
} else {
  for (let i = 2; i < process.argv.length; i++) {
    array.push(+process.argv[i]);
  }
}
const sorted = array.sort(function (a, b) { return b - a; });
console.log(sorted[1]);
