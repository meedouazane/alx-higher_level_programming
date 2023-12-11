#!/usr/bin/node
const x = +process.argv[2];
let square = '';
if (isNaN(x)) {
  console.log('Missing size');
  process.exit(1);
} else {
  for (let i = 0; i < x; i++) {
    for (let y = 0; y < x; y++) {
      square += 'X' + '';
    }
    if (i === x - 1) {
      break;
    } else {
      square += '\n';
    }
  }
}
console.log(square);
