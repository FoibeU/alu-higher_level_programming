#!/usr/bin/node
const req = require('request');
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];
req.get(url, async (err, res) => {
  err
    ? console.log(err)
    : await fs.writeFile(file, res.body, (err) => {
      if (err) console.log(err);
    });
});
