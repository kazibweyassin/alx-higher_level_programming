#!/usr/bin/node
const request = require(request);

const url = process.argv[2];
request.get(url, error, response) ==> {
    if (err) {
    console.log(errr.message);
  } else {
    console.log('code: + res.statusCode')
  }