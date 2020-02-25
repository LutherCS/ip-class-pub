/* jshint esversion: 8 */
/* jshint node: true */
'use strict';

class ComputerMouse {
    constructor(nButtons, cType, color) {
        this._buttons = nButtons;
        this._connection = cType;
        this._color = color;
    }

    get buttons() {
        return this._buttons;
    }

    get connectionType() {
        return this._connection;
    }

    set connectionType(newValue) {
        this._connection = newValue;
    }

    get color() {
        return this._color;
    }

    set color(newValue) {
        this._color = newValue;
    }

    paint(newColor) {
        this._color = newColor;
    }

    toString() {
        return `A ${this._color} ${this._connection} mouse with ${this._buttons} buttons`;
    }
}

// let m = new ComputerMouse(3, "wired", "black");
// console.log(m);
// m.connectionType = "wireless";
// console.log(m);
// m.paint("green");
// console.log(m);
// m.buttons = 5;
// console.log(m);
// console.log(m.toString());

class Lab {
    constructor(theSize) {
        this._size = theSize;
        this._lab = [];
    }

    add (mouse) {
        if (this._lab.length < this._size) {
            this._lab.push(mouse);
        }
    }

    [Symbol.iterator]() {
        let idx = -1;
        return {
            next: () => ({value: this._lab[++idx], done: !(idx in this._lab)})
        };
    }
}

let olin202 = new Lab(2);
let m1 = new ComputerMouse(1, "wired", "black");
let m2 = new ComputerMouse(3, "wireless", "green");

olin202.add(m1);
olin202.add(m2);
console.log(olin202);

for (let m of olin202) {
    console.log(m.toString());
}

console.log("Empty lab");
let olin112 = new Lab(0);
for (let m of olin112) {
    console.log(m.toString());
}
