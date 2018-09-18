/* jshint esversion: 6 */
/* jshint node: true */

'use strict';

class Can {
    constructor(radius, height) {
        this._radius = radius;
        this._height = height;
    }

    get volume() {
        return Math.PI * this._radius * this._radius * this._height;
    }

    set volume(new_value) {
        console.error('Don\'t!');
    }

    get radius() {
        return this._radius;
    }

    get height() {
        return this._height;
    }

    set height(new_value) {
        if (new_value <= 0) {
            console.error('Be positive!');
        } else {
            this._height = new_value;
        }
    }

    toString() {
        return `A can of radius ${this._radius} and height of ${this._height}`;
    }
}

class Case {
    constructor() {
        this._case = [];
        for (let i = 0; i < 6; i++) {
            this._case.push(new Can(1, 5));
        }
    }
    [Symbol.iterator]() {
        let i = -1;
        return {
            next: () => ({value: this._case[++i], done: !(i in this._case)})
        };
    }
}

let pepsi = new Can(2, 6);
console.log(pepsi.volume);
pepsi.volume = 80;
console.log(pepsi.volume);
pepsi.height = 10;
console.log(pepsi.volume);
console.log(pepsi.toString());

let pepsi_case = new Case();
for (let p of pepsi_case) {
    console.log(`${p.toString()} has volume of ${p.volume}`);
}
