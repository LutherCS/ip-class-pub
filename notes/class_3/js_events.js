/* jshint esversion: 8 */
/* jshint node: true */
/* jshint browser: true */
'use strict';

console.log("Hello from the console");

document.writeln("Hello from the canvas");

function addParagraph() {
    let c = document.querySelector("#content");
    let p = document.createElement("p");
    p.classList = "para";
    p.setAttribute("id", "third");
    p.innerHTML = "This is a new paragraph";
    c.append(p);
}

function doSomething(new_color) {
    let the_color = new_color || 'green';
    let all_p = document.querySelectorAll(".para");
    for (let p of all_p) {
        p.setAttribute("style", `color:${the_color}`);
    }
}

function greetByName() {
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    // console.log(urlParams);
    let name = urlParams.get('name');
    let color = urlParams.get('color');
    let greet = document.querySelector("h1");
    greet.innerHTML = `Hello ${name}`;
    doSomething(color);
}

window.onload = function() {
    addParagraph();
    this.greetByName();
};
