"use strict;"

function nextPrime() {
    let number = document.querySelector("#nextprime");
    let currentPrime = number.innerHTML;

    if (currentPrime === "&nbsp;") {
        currentPrime = 1;
    }

    number.innerHTML = getNextPrime(currentPrime).toString();
}

function getNextPrime(n) {
    let nextPrimeNumber = parseInt(n) + 1;
    while (!isPrime(nextPrimeNumber)) {
        nextPrimeNumber++;
    }
    return nextPrimeNumber;
}

function isPrime(n) {
    for (let i = 2; i < n / 2 + 1; i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

function reset() {
    let number = document.querySelector("#nextprime");
    number.innerHTML = "&nbsp;";
}