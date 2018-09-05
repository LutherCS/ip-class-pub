/* jshint esversion: 6 */
"use strict";

function isPrime(n) {
    for (let i = 2; i < n / 2; i++) {
        if (n % i === 0) {
            return false;
        }
    }
    return true;
}