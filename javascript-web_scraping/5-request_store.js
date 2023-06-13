#!/usr/bin/node
const requests = require('request');
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];
requests.get(url, async (error, result) => {
  error
    ? console.log(error)
    : await fs.writeFile(file, result.body, (error) => {
      if (error) console.log(error);
    });
});
