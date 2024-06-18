#!/usr/bin/node
const args = process.argv.slice(2);
const ArgsCount = args.length;
if (ArgsCount === 0) {
  console.log('No argument');
} else {
  console.log(args);
}
