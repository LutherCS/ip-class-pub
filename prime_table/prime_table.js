/* jshint esversion: 6 */
"use strict";

function isPrime(n) {
    for (let i = 2; i <= n / 2; i++) {
        if (n % i === 0) {
            return false;
        }
    }
    return true;
}

function getNPrimes(n) {
    let primes = [];
    let i = 1;
    while (primes.length < n) {
        i = i + 1;
        if (isPrime(i)) {
            primes.push(i);
        }
    }
    return primes;
}

function generateTableOfPrimes() {
    let all_params = new URLSearchParams(window.location.search);
    let n = parseInt(all_params.get('n'));
    let my_table = document.querySelector('#primetbl');
    let my_primes = getNPrimes(n);

    for (let p of my_primes) {
        let row = document.createElement('tr');
        let cell = document.createElement('td');
        cell.innerHTML = p;
        row.appendChild(cell);
        my_table.appendChild(row);
    }
}
