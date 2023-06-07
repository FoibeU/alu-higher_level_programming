#!/usr/bin/node
const number = process.argv[2];
const Intnumber = (parseInt(number));

if (Intnumber) {
  console.log(`My number: ${parseInt(Intnumber)}`);
} else {
  console.log('Not a number');
}
