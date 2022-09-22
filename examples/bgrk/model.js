/* jshint esversion: 8 */
/* jshint strict: true */
/* jshint node: true */
"use strict";

class Game {
    constructor(title, designer, publisher, price, purchased, rating) {
        this._title = title;
        this._designer = designer;
        this._publisher = publisher;
        this._price = price;
        this._purchased = purchased;
        this._rating = rating;
    }

    get title() {
        return this._title;
    }
    get designer() {
        return this._designer;
    }
    get publisher() {
        return this._publisher;
    }
    get price() {
        return this._price;
    }
    get purchased() {
        return this._purchased;
    }
    get rating() {
        return this._rating;
    }
    set rating(newValue) {
        this._rating = newValue;
    }

    toString() {
        return `${this._title} by ${this._designer}`;
    }
}

class Subject {
    constructor() {
        this.handlers = [];
    }

    subscribe(func) {
        this.handlers.push(func);
    }

    publish(msg, obj) {
        let scope = obj || window;
        for (let func of this.handlers) {
            func(scope, msg);
        }
    }
}

class Library extends Subject {
    constructor() {
        super();
        this._collection = [];
    }

    add(newGame) {
        this._collection.push(newGame);
        console.log(`Model just added ${newGame.toString()}`);
        this.publish(`A new game (${newGame.toString()}) has been added`, this);
    }

    [Symbol.iterator]() {
        let index = -1;
        return {
            next: () => ({ value: this._collection[++index], done: !(index in this._collection) })
        };
    }

    get length() {
        return this._collection.length;
    }
}

