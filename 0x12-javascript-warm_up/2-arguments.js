#!/usr/bin/node
const args = process.argv.slice(2);
const ArgsCount = args.length;
if (ArgsCount === 0) {
  console.log('No argument');
} else if (ArgsCount === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
