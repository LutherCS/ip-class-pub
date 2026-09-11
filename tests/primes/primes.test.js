/**
 * Testing primes
 * 
 * @author: Roman Yasinovskyy
 * @version: 2026.9
 * 
 * @jest-environment jsdom
 */
"use strict";

const primes = require('../../exercises/primes/main');

/**
 * Test isPrime
 */
const testData_isPrime = [[1, false], [2, true], [3, true], [5, true], [10, false]];
test.each(testData_isPrime)("Checking primality of %s to be %s", (number, expected) => {
    expect(primes.isPrime(number)).toBe(expected);
});

/**
 * Test getNPrimes
 */
const testData_getNPrimes = [
    [1, [2]],
    [2, [2, 3]],
    [3, [2, 3, 5]],
    [5, [2, 3, 5, 7, 11]],
    [10, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]],
];
test.each(testData_getNPrimes)("Generating %s prime(s) to be %s", (number, expected) => {
    expect(primes.getNPrimes(number)).toStrictEqual(expected);
});
