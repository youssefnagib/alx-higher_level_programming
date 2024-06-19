#!/usr/bin/node
const a = process.argv[2];
function factorial (a) {
  if (a === undefined || a === 1) {
    console.log('1');
  } else {
    let result = 1;
    for (let i = 0; i < a; i++) {
      result = (a - i) * result;
    }
    return result;
  }
}
console.log(factorial(a));
