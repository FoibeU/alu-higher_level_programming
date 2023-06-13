#!/usr/bin/node
const requests = require('request');
requests.get(process.argv[2], (error, result) => {
 if(error) {console.log(error);
  }else{ console.log('code: ' + result.statusCode);
}
});