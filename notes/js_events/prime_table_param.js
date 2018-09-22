/* jshint esversion: 6 */
/* jshint node: true */
"use strict";

$(document).ready(function () {
    let all_params = new URLSearchParams(window.location.search);
    let n = parseInt(all_params.get('n'));
    generateTableOfPrimes('#primetbl', n);
});
