/* jshint esversion: 6 */
/* jshint node: true */
'use strict';

// document.writeln("writing something");

function startEverything() {
    console.log("It's started!");
}

function doSomething() {
    let btn = document.querySelector("#theButton");
    let inputField1 = document.querySelector("#number1");
    let number = parseInt(inputField1.value);

    if (isNaN(number)) {
        number = 330;
    }

    btn.innerHTML = `You entered ${number}`;
    let answerElement = document.querySelector("#answer");
    answerElement.innerHTML = `Incremented by 1 ${number} is ${number + 1}`;
    let evenCheckElement = document.querySelector("#evenCheck");
    if (isEven(number)) {
        evenCheckElement.innerText = `${number} is even`;
    } else {
        evenCheckElement.innerText = `${number} is odd`;

    }
    
}

window.onload = function() {
    this.startEverything();
}

// Must have jQuery for this to work
// $(document).ready(function() {
//     startEverything();
// });