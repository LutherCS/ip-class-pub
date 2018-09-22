/* jshint esversion: 6 */
/* jshint node: true */
"use strict";

function clickedon() {
    let n = parseInt(document.querySelector('#numprimes').value);
    generateTableOfPrimes('#primetbl', n);
}
