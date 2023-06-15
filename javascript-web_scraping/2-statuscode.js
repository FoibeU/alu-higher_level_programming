#!/usr/bin/node
const requests = require('request');
requests.get(process.argv[2], (error, results) => {
  error ? console.log(error) : console.log('code: ' + results.statusCode);
});
