#!/usr/bin/node
function factorial (a) {
  if (a <= 1) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}
let number = process.argv[2];
if (isNaN(number)) {
  number = 1;
}
const f = factorial(number);
console.log(f);
