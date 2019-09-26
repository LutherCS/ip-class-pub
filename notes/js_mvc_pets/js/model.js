/* jshint esversion: 6 */
/* jshint node: true */
/* jshint browser: true */
'use strict';

class Cat {
    constructor(some_name, some_place, legs = 4, diet = "everything") {
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
    constructor () {
        this.handlers = [];
    }

    subscribe(func) {
        this.handlers.push(func);
    }

    unsubscribe(func) {
        this.handlers = this.handlers.filter(item => item != func);
    }

    publish(msg, obj) {
        let scope = obj || window;
        for (let f of this.handlers) {
            f(scope, msg);
        }
    }

}

class Clowder extends Subject {
    constructor(size) {
        super();
        this._clowder = [];
    }

    adopt(cat) {
        this._clowder.push(cat);
        this.publish("new cat added", this);
    }

    [Symbol.iterator]() {
        let idx = -1;
        return {
            next: () => ({ value: this._clowder[++idx], done: !(idx in this._clowder) })
        };
    }

    cleanList() {
        this._clowder = this._clowder.filter(aCat => aCat.removed);
        this.publish("cat(s) removed", this);
    }

    toString() {
        return `${this._clowder}`;
    }

    get size() {
        return this._clowder.length;
    }
}
