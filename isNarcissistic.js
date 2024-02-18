function isNarcissistic(n) {
    if (n < 10) { return true; } // Single digit numbers are considered narcissistic.
    let count = 0;
    let sum = 0;
    let n_copy = n;
    const digits = [];
  
    // Extract digits of n and count them.
    while (n_copy > 0) {
      digits.push(n_copy % 10);
      n_copy = Math.floor(n_copy / 10);
      count++;
    }
  
    // Calculate the sum of digits each raised to the power of count (number of digits).
    sum = digits.reduce((accumulator, currentValue) => accumulator + Math.pow(currentValue, count), 0);
  
    // Check if the sum is equal to the original number.
    return sum === n;
  }
  