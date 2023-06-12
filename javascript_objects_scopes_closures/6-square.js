#!/usr/bin/node
const pClass = require('./5-square');
class Square extends pClass {
  charPrint (c) {
    if (c !== undefined) {
      for (let j = 0; j < this.height; j++) {
        console.log(c.repeat(this.width));
      }
    } else {
      this.print();
    }
  }
}
module.exports = Square;
