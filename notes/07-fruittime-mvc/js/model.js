"use strict";

class Food {
    #name;
    constructor(name) {
        this.#name = name;
    }

    get name() { return this.#name; }

}

class Fruit extends Food {
    #onTree;
    constructor(name, onTree) {
        super(name);
        this.#onTree = onTree;
    }

    toString() {
        if (this.#onTree) {
            return `${this.name} grows on tree`;
        } else {
            return `${this.name} does not grow on tree`;
        }
    }

    toJSON() { return { "name": this.name, "onTree": this.#onTree }; }
}

class Review {
    #food;
    #rating;
    #opinion;
    constructor(food, rating, opinion) {
        this.#food = food;
        this.#rating = rating;
        this.#opinion = opinion;
    }

    get food() { return this.#food; }
    get rating() { return this.#rating; }
    set rating(newValue) { this.#rating = newValue; }

    get opinion() { return this.#opinion; }
    set opinion(newValue) { this.#opinion = newValue; }

    toString() { return `${this.#food} is ${this.#opinion}`; }

    toJSON() { return { "food": this.#food, "rating": this.#rating, "opinion": this.#opinion } }
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
        for (let f of this.handlers) {
            f(scope, msg);
        }
    }
}

class CollectionOfReviews extends Subject {
    #collection;

    constructor() {
        super();
        this.#collection = [];
    }

    add(review) {
        this.#collection.push(review);
        this.publish("A new review has been added", this);
    }

    get reviews() { return this.#collection; }

    [Symbol.iterator]() {
        // return this.#collection[Symbol.iterator]();
        let idx = 0;
        return {
            next: () => ({ value: this.#collection[idx++], done: idx > this.#collection.length }),
        }
    }
}
