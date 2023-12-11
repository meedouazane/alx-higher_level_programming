#!/usr/bin/node
let i = 0;
exports.callMeMoby = (x, theFunction) => {
  while (i < x) {
    console.log('C is fun');
    i++;
  }
};
