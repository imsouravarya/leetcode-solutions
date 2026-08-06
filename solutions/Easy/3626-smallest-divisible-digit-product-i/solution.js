/**
 * @param {number} n
 * @param {number} t
 * @return {number}
 */
var smallestNumber = function(n, t) {
  while (true) {
    let product = String(n)
      .split('')
      .reduce((acc, digit) => acc * Number(digit), 1);

    if (product % t === 0) {
      return n;
    }

    n++;
  } 
}; 