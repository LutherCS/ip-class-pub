/* jshint esversion: 8 */
/* jshint node: true */
/* jshint browser: true */
'use strict';


/**
 * Greet user by name
 * 
 * @param {string} name visitor's name
 * @param {string} selector element to use for display
 */
function greet(name, selector) {}


/**
 * Check if a number is prime
 * 
 * @param {number} number number to check
 * @return {boolean} result of the check
 */
function isPrime(number) {}


/**
 * Print whether a number is prime
 * 
 * @param {number} number number to check
 * @param {string} selector element to use for display
 */
function printNumberInfo(number, selector) {}


/**
 * Generate an array of prime numbers
 * 
 * @param {number} number number of primes to generate
 * @return {number[]} an array of `number` prime numbers
 */
function getNPrimes(number) {}


/**
 * Print a table of prime numbers
 * 
 * @param {number} number number of primes to display
 * @param {string} selector element to use for display
 */
function printNPrimes(number, selector) {}


/**
 * Display warning about missing URL query parameters
 * 
 * @param {Object} urlParams URL parameters
 * @param {string} selector element to use for display
 */
function displayWarnings(urlParams, selector) {}

window.onload = function () {
    // TODO: Initialize the following variables
    let urlParams = "";
    let name = "";
    let number = "";
    this.displayWarnings(urlParams, "#warnings");
    greet(name, "#greeting");
    printNumberInfo(number, "#numberInfo");
    printNPrimes(number, "table#nPrimes");
};
