
console.log("Hello, CS330!")

console.log(dog1)  // dog1 is hoisted
var dog1 = "Poodle"
console.log(dog1)
dog1 = "Husky"
console.log(dog1)

// console.log(dog2)  // dog2 is NOT hoisted
let dog2 = "Poodle"
console.log(dog2)
console.log(dog2 + 1)
console.log(dog2 + "1")

// console.log(dog3)  // dog3 is NOT hoisted
const dog3 = "Poodle"
console.log(dog3)
// dog3 = "Husky"  // const cannot be changed
console.log(dog3)

let n = 2
console.log(n);
console.log(n + 1);
console.log(n + "1");

let roster = [6, 7, 61, "Alice", "Aardvark", true]
console.log(roster);
roster.sort()
console.log(roster);

for (let name in roster) {
    console.log(name);
}

for (let name of roster) {
    console.log(name);
}

for (let idx in roster) {
    console.log(idx, roster[idx]);
}

roster.push(null)
console.log(roster);
console.log(roster.pop())
console.log(roster);

if (61 < 7) {
    console.log("A");
} else {
    console.log("B");
}

let roster2 = {}
roster2["Alice"] = "aardvark"
roster2["Bob"] = "beaver"
roster2["Charlie"] = "cheetah"
console.log(roster2);
roster2[1] = "the_one"
console.log(roster2[1]);
console.log(roster2['1']);
console.log(roster2["1"]);

let m = 12
console.log(m == 12);  // true
console.log(m == "12");  // true
console.log(m === "12");  // false
console.log(Boolean(""));  // false
console.log("" == null);  // false
console.log("" == false);  // true
console.log("" === false);  // false
console.log("" !== false);  // true
console.log(Boolean(NaN));  // false

function add(number) {
    console.log(`Adding 1 to ${number}`);  // use ticks
    return number + 1
}

let a = 12
console.log(a);
let b = add(a)
console.log(b);
