#!/usr/bin/node
const a = process.argv[2];
function factorial (a) {
  if (a === undefined || a === 0) {
    return '1';
  } else {
    let result = 1;
    for (let i = 1; i <= a; i++) {
      result *= i;
    }
    return result;
  }
}
console.log(factorial(a));
