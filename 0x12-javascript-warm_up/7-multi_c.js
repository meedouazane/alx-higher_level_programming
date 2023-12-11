#!/usr/bin/node
let i = 0;
const x = +process.argv[2];
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  while (i < process.argv[2]) {
    console.log('C is fun');
    i++;
  }
}
