/* jshint esversion: 6 */
/* jshint node: true */
"use strict";

var h = "hello";

function add(a, b) {
    return a + b;
}

var mylist = [1, 2, 'hello', true];
console.log('Size of the array: ' + mylist.length);
console.log(mylist);

console.log('Iterating over an array keys');
for (let k in mylist) {
    console.log(k);
}
console.log('Iterating over an array values');
for (let k of mylist) {
    console.log(k);
}

// print(k);  // Throws an error

let mydict = {};
mydict[1] = 'hello';
mydict.a = 42;
mydict[2] = 15;

console.log('Size of the dictionary: ' + Object.keys(mydict).length);
console.log(mydict);

const PI = 3.15;
console.log(PI);
// PI = 4;  // throws an error
