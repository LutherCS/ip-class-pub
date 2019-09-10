/* jshint esversion: 6 */
/* jshint node: true */
/* jshint browser: true */
"use strict";

console.log('hello');

const x = [1, 2, 3];
console.log(x);

x.push(4);
console.log(x);

hello("Classs of CS330");
hello();

let a = 5;

console.log(a);
console.log(add1(a));
add1(a);
console.log(a);

let b = "hello";
console.log(b);
console.log(add1(b));

console.log(add1());

/* ONLY WORKS IN A BROWSER */
// document.writeln('hello');
// document.write('hello\n');

function hello(name) {
    console.log("Hello, " + name);
}

function add1(n) {
    return n + 1;
}

console.log(1 == 1);
console.log(1 == '1');
console.log(1 == "1");
console.log(1 === "1");
console.log("" == null);
console.log("" == NaN);
console.log(null == undefined);

let age = 142;

if (age > 21) {
    console.log("BOO");
    console.log("Second");
} else if (age > 65) {
    console.log("HOO");
} else {
    console.log("FOO");
}

let c = 45;

switch (c) {
    case 1:
        console.log("One");
        break;
    case 2:
        console.log("Two");
        break;
    case 3:
        console.log("Three");
        break;
    case 4:
        console.log("Four");
        break;
    case 5:
        console.log("Five");
        break;
    case 6:
        console.log("Six");
        break;
    case 7:
        console.log("Seven");
        break;
    default:
        console.log("Unknown number?!");
}

let d = {1: "One", 2: "Two"};
d[3] = "Three";
d.four = "Four";

console.log(d[1]);
console.log(d.four);

console.log(d);
console.log(d.four);
console.log(d["four"]);

console.log(Object.keys(d));

let roster = ["Alice", "Bob", "Chuck"];

for (let idx in roster) {
    console.log(roster[idx]);
}

for (let name of roster) {
    console.log(name);
}

/* ONLY WORKS IN A BROWSER */
// let params = new URLSearchParams(window.location.search);
// let n = params.get("n");
// document.write(n);
