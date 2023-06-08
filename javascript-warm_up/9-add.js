#!/usr/bin/node
function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    return 'NaN';
  } else {
    const sum = a + b;
    return ` ${sum}`;
  }
}

const argvalue = process.argv.slice(2);
const n1 = parseInt(argvalue[0]);
const n2 = parseInt(argvalue[1]);

console.log(add(n1, n2));
