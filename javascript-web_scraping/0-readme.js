#!/usr/bin/node
const fs = require('fs');
const file = process.argv.slide(2)[0];
fs.readFile(file, 'utf8', (error, contents) =>{
    if (err){
        console.log(error);
    }else{
        console.log(contents);
    }
})
