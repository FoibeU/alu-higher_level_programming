#!/usr/bin/node
function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    return 'Invalid numbers';
  } else {
    const sum = a + b;
    return `The sum of ${a} and ${b} is: ${sum}`;
  }
}

const argvalue = process.argv.slice(2);
const n1 = parseInt(argvalue[0]);
const n2 = parseInt(argvalue[1]);

console.log(add(n1, n2));
