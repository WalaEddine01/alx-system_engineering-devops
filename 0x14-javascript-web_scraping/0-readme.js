#!/usr/bin/node

const fs = require('fs');
const { argv } = require('process');

console.log(fs.readFileSync(argv[2], 'utf-8'));
