#!/usr/bin/node
const args = process.argv.slice(2);
args[0] = parseInt(args[0]);
if (!Number(args[0])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(args[0]));
}
