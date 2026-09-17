"use strict;"
console.log("Hello, CS330!");
console.log('Hello again');

let a = 35.5;
console.log(a);
const b = "100";
console.log(b);
console.log("The sum of a and b is " + a + b);
console.log(a + b);
console.log(b + a);
console.log(`The value of a id ${a}`);
console.log(a > b);
if (a > b) {
    console.log("a is greater");
} else if (a < b) {
    console.log("b is greater");
} else {
    console.log("they are equal!");
}

while (a < 50) {
    console.log(a);
    a++;
}
for (let i = 0; ; i++) {
    if (i == 32) {
        console.log("and we are done!");
        break;
    }
}
// console.log(i);

const groceries = ["milk", "eggs", "cheese", 4, a, null, false]
console.log(groceries);
groceries[6] = true;
console.log(groceries);
// groceries = "Food"
groceries.pop();
groceries.push("yipee");
console.log(groceries);
for (let item in groceries) {
    console.log(item);
}
for (let item of groceries) {
    console.log(item);
}
groceries.sort();
console.log(groceries);
const numbers = [100, 2, 11, 3, 1415926, "five", true, null, false]
numbers.sort((n1, n2) => n1 - n2)
console.log(numbers);
const dict = { "eggs": 4.99, "milk": 2.39, "cheese": "depends" }
for (let item in dict) {
    console.log(item);
    console.log(dict[item]);

}

function myf(a, b) {
    console.log(a + b);
    console.log(a);
    console.log(b);

}
myf(2, 3);
myf("two", "three");
myf(true);

// A simple check to see whether browser objects are available
if (typeof window !== 'undefined') {
    window.onload = function () {
        let greeting = document.querySelector("#greeting");
        greeting.innerHTML = "Go home";
        let newP = document.createElement("p");
        newP.innerHTML = "I'm new here";
        greeting.parentElement.appendChild(newP);
    }
} else {
    console.log("window object is not available");
}
