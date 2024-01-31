#!/usr/bin/node
const request = require('request');

request('http://google.com/doodle.png').pipe(fs.createWriteStream('doodle.png'))