/* jshint esversion: 6 */
/* jshint node: true */
'use strict';

class Cat {
    constructor(some_name, legs = 4, some_place, diet = "everything") {
        this._name = some_name;
        this._nLegs = legs;
        this._habitat = some_place;
        this._diet = diet;

        this._removed = false;
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

    get habitat() {
        return this._habitat;
    }

    set habitat(new_value) {
        console.log("Error. Cannot set habitat");
    }

    get diet() {
        return this._diet;
    }

    set diet(new_value) {
        console.log("Error. Cannot set diet");
    }

    get removed() {
        return this._removed;
    }

    set removed(newValue) {
        this._removed = newValue;
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

class Subject {
    /* TODO */

}

class Clowder extends Subject {
    constructor(size) {
        super();
        this._clowder = [];
    }

    adopt(cat) {
        this._clowder.push(cat);
    }

    [Symbol.iterator]() {
        let idx = -1;
        return {
            next: () => ({ value: this._clowder[++idx], done: !(idx in this._clowder) })
        };
    }

    cleanList() {
        /* TODO */

    }

    toString() {
        return `${this._clowder}`;
    }

    get size() {
        return this._clowder.length;
    }
}
