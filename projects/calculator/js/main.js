/* jshint esversion: 8 */
/* jshint browser: true */
'use strict';

var outputScreen;
var clearOnEntry;


/**
 * Display a digit on the `outputScreen`
 * 
 * @param {number} digit digit to add or display on the `outputScreen`
 */
function enterDigit(digit) {}


/**
 * Clear `outputScreen` and set value to 0
 */
function clear_screen() {}


/**
 * Evaluate the expression and display its result or *ERROR*
 */
function eval_expr() {}


/**
 * Display an operation on the `outputScreen`
 * 
 * @param {string} operation to add to the expression
 */
function enterOp(operation) {}


window.onload = function () {
    outputScreen = document.querySelector("#result");
    clearOnEntry = true;
};
