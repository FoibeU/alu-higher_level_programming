#!/usr/bin/node
let count = 0;

const logMe = (Item) => {
  console.log(count + ': ' + Item);
  count++;
};
exports.logMe = logMe;
