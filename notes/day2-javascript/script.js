/* jshint esversion: 8 */


console.log("Hello");

const a = 330;
console.log(a);
console.log(a + 1);
console.log(a + "1");

// The following line yields an error
// a = a + 1;
// console.log(a);

const roster = [1, 2, "Alice", true];
console.log(roster);
roster.push("Bobo");
console.log(roster);
roster.pop();
console.log(roster);

for (let index in roster) {
    console.log(index, roster[index]);
}

for (let item of roster) {
    console.log(item);
}

if (roster.length < 5) {
    console.log("Not enough items");
}

while (roster.length < 10) {
    console.log("Too few items");
    roster.push(330);
}

console.log("there are " + roster.length + " items in the roster");
console.log(`there are ${roster.length} items in the roster`);
console.log(roster);

let b = 42;
if (b > 0) {
    console.log(`${b} is positive`);
} else if (b < 0) {
    console.log(`${b} is negative`);
} else {
    console.log(`${b} is 0`);
}

let c = 22;
switch (c) {
    case 1:
        console.log("January");
        break;
    case 2:
        console.log("February");
        break;
    case 12:
        console.log("December");
        break;
    default:
        console.log("Unknown month");
}

let d = {};
d[1] = "Alice";
d[2] = "Bob";
d["3"] = true;
console.log(d);
console.log(d[1]);
console.log(d["1"]);
console.log(d['1']);

let e = 5;
console.log(e == 5);
console.log(e == "5");
console.log(e === "5");
console.log("" == null);
console.log(Boolean(""));
console.log(undefined == NaN);

function hello(name) {
    // console.log(`Hello, ${name}`);
    return `Hello, ${name}`;
}

console.log(hello("330"));
