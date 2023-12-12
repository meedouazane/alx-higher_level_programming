#!/usr/bin/node

const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

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
