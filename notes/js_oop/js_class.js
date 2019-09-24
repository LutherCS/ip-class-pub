/* jshint esversion: 6 */
/* jshint node: true */
'use strict';

class Cat {
    constructor(some_name, some_place) {
        this._name = some_name;
        this._nLegs = 4;
        this._diet = "everything";
        this._habitat = some_place;
    }

    get name() {
        return this._name;
    }

    set name(new_value) {
        this._name = new_value;
    }

    get legs() {
        return this._nLegs;
    }

    set legs(new_value) {
        console.log("Error. Cannot set number of legs, use amputate()");
    }

    amputate() {
        this._nLegs--;
    }

    grow() {
        this._nLegs++;
    }

    toString() {
        return `${this._name} has ${this._nLegs} legs, lives in the ${this._habitat}, and eats ${this._diet}`;
    }
}
// c.color = "black";

let c = new Cat("Hairy Harry", "kitchen");
console.log(c);

console.log(c.name);
c.name = "Black Beauty";
console.log(c.name);

console.log(c.toString());
c.legs = 5;
console.log(c.toString());
c.amputate();
console.log(c.toString());
c.grow();
c.grow();
c.grow();
console.log(c.toString());

class Clowder{
    constructor(size) {
        this._clowder = [];
    }

    adopt(cat) {
        this._clowder.push(cat);
    }

    [Symbol.iterator]() {
        let idx = -1;
        return {
          next: () => ({ value: this._clowder[++idx], done: !(idx in this._clowder)})
        };
    }

    toString() {
        return `${this._clowder}`;
    }
}

let cl = new Clowder(3);
console.log(cl.toString());
cl.adopt(c);
console.log(cl.toString());
cl.adopt(new Cat("Sophie", "living room"));

for (let cat of cl) {
    console.log(cat.toString());
}