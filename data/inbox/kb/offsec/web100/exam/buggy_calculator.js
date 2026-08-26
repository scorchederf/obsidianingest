/**
 * Buggy Calculator v1.3.3.7
 * Brought to you by Offensive Security.
*/

/**
 * Computes the sum of two operands.
 * @param  {number} x The first addend.
 * @param  {number} y The second addend.
 * @return {number} The sum of x and y.
*/
function add(x, y) {
    sum = x + y;
    return sum;
}

/**
 * Computes the difference of two operands.
 * @param  {number} x The minuend of the subtraction.
 * @param  {number} y The subtrahend of the subtraction.
 * @return {number} The difference of x and y.
*/
function subtract(x, y) {
    var diff = x - y;
    return diff;
}

/**
 * Computes the product of two operands.
 * @param  {number} x The first multiplier.
 * @param  {number} y The second multiplier.
 * @return {number} The product of x and y.
*/
function multiply(x, y) {
    var product = x * y;
    return product;
}

/**
 * Computes the ratio of two operands.
 * @param  {number} x The dividend of the division.
 * @param  {number} y The divisor of the division.
 * @return {number} The ratio of x and y.
*/
function divide(x, y) {
    return x / y;
}
