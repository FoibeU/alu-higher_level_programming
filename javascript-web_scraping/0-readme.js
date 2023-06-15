#!/usr/bin/node
const fs = require('fs');

fs.readFile(process.argv[2], (error, contents) => {
  error ? console.log(error) : console.log(contents.toString());
});

