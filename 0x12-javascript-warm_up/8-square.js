#!/usr/bin/node
const row = parseInt(process.argv[2]);
if (isNaN(row)) {
  console.log('Missing size');
} else {
  let z = 0;
  while (z < row) {
      let x = '';
    for (let i = 0; i < row; i++) {
      x += 'x';
    }
    console.log(x);
    z += 1;
  }
}
