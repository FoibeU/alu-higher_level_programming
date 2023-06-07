#!/usr/bin/node
const argValue = process.argv[2];

if (argValue) {
  console.log(argValue);
} else {
  console.log('No argument');
}
