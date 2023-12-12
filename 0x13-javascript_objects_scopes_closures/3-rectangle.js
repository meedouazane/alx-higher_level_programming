#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w === undefined || h === undefined || w <= 0 || h <= 0) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    let square = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        square += 'X' + '';
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
module.exports = Rectangle;
