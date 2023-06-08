#!/usr/bin/node
const argValue = process.argv.slice(2);
const x = parseInt(argValue[0]);

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
