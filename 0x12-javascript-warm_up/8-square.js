#!/usr/bin/node
const x = process.argv[2];
if (!Number(x)) {
  console.log('Missing size');
} else {
  let z = 0;
  let row = '';
  while (z < x) {
    for (let i = 0; i < x; i++) {
      row += 'x';
    }
    console.log(row);
    row = '';
    z += 1;
  }
}
