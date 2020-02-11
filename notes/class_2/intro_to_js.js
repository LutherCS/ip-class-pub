/* jshint esversion: 8 */
/* jshint node: true */
'use strict';

console.log("Hello " + "CS" + 330);
console.log('Hello again');
console.log("Hello number 4");
console.log("1" + 2);

let x = 5;
console.log(x);

const boo = [1, 2, 'hello', true];
console.log(boo);

boo.push(4);
console.log(boo);

console.log(boo.pop());
console.log(boo);

for (let i in boo) {
    console.log(i);
}

for (let i of boo) {
    console.log(i);
}

for (let i in boo) {
    console.log(boo[i]);
}

let y = 4;

console.log(y == 4);
console.log(y === '4');
console.log("" == null);
console.log(NaN == undefined);

let foo = -4;

if (foo > 0) {
    console.log("positive");
 } else if (foo < 0) {
    console.log("negative");
    console.log("very negative");
} else 
    console.log("zero");


let turkey = 11;

switch (turkey) {
    case 1:
        console.log("January");
        break;
    case 11:
        console.log("November");
        break;
    case 12:
        console.log("December");
        break;
}

let a = 10;

while (a > 0) {
    console.log(a);
    --a;
}

function hello(name) {
    console.log(`Hello, ${name}`);
}

hello("CS330");

let dFoo = {"Alice": 5, "Bob": 3, "Chuck": 5}
console.log(dFoo["Alice"]);
console.log(dFoo.Bob);
