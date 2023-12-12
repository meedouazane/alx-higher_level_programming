#!/usr/bin/node

exports.esrever = function (list) {
  const newlist = [];
  let y = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    newlist[y] = list[i];
    y++;
  }
  return newlist;
};
