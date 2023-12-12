#!/usr/bin/node
const SquareC = require('./5-square');
class Square extends SquareC {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let square = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        square += c + '';
      }
      if (i === this.height - 1) {
        break;
      } else {
        square += '\n';
      }
    }
    console.log(square);
  }
}
module.exports = Square;
