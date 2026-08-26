//Returns true whether the val input is a prime number, and false otherwise
function isPrime(val) {
    var isprime = true;
    for(var j = 2; j <= val; j++) {
            if(val % j === 0 && j != val) {
                    isprime = false;
            }
    }
    return isprime;
}

function primeCalc(num1, num2) {
// this function is given 2 arguments as numbers, where num1 can be assumed to always be strictly less than num2, and both numbers are greater than 1.
// we will have to write code to do the following:
// Find all prime numbers between num1 and num2, inclusive, and return an array of these prime numbers in ascending order.
// Note: You may use the isPrime function to determine whether a number is prime or not.
// Hint: the push function can add elements to an array. For example, after running var a = [1, 2]; a.push(3);, a should contain [1, 2, 3].
// Once you think you got a working implementation, run `sudo /usr/bin/node /home/student/primeCalc_test.js` to get the flag!`

    const primes = [];
    for (let num = num1; num <= num2; num++) {
        if (isPrime(num)) {
          primes.push(num);
        }
      }



return primes;
}

module.exports = { primeCalc }
