#!/usr/bin/node
const row = parseInt(process.argv[2]);
if (!Number(row)) {
  console.log('Missing size');
} else {
  let z = 0;
  let x = '';
  while (z < row) {
    for (let i = 0; i < row; i++) {
      x += 'x';
    }
    console.log(x);
    x = '';
    z += 1;
  }
}
