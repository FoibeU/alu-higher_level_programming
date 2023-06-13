#!/usr/bin/node
const requests = require('request');
const url = process.argv[2];

let count = 0;
let value;
requests.get(url, (error, result) => {
  if (error) console.log(error);
  else {
    value = JSON.parse(result.body).results;
    value.forEach((objects) => {
      objects.characters.forEach((character) => {
        if (character.includes('/18/')) count++;
      });
    });
  }
  console.log(count);
});
