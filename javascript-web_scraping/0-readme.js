#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[2], 'utf-8', (error, contents) =>{
    if (error){
        console.log(error);
    }else{
        console.log(contents.toString());
    }
})
