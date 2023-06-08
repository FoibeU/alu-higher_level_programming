#!/usr/bin/node
const argValue = process.argv.slice(2);
const n = parseInt(argValue[0]);

if (isNaN(n)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < n; i++) {
    let row = '';
    for (let j = 0; j < n; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
