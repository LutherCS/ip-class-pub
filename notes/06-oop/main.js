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

    get rating() { return this.#rating; }
    set rating(newValue) { this.#rating = newValue; }

    get opinion() { return this.#opinion; }
    set opinion(newValue) { this.#opinion = newValue; }

    toString() { return `${this.#food} is ${this.#opinion}`; }

    toJSON() { return { "food": this.#food, "rating": this.#rating, "opinion": this.#opinion } }
}

class CollectionOfReviews {
    #collection;

    constructor() {
        this.#collection = [];
    }

    add(review) {
        this.#collection.push(review);
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
let meal = new Food("lunch");
console.log(meal);
meal.taste = "ok";  // creates new attribute
console.log(meal);

let apple = new Fruit("apple", true);
let tomato = new Fruit("tomato", false);
console.log(apple.toString());
console.log(`${apple}`);

let feedback = new Review(apple, 4, "better than average");
let feedback2 = new Review(tomato, 2, "meh");
console.log(feedback.toString());
console.log(JSON.stringify(feedback, null, 2));

let cor = new CollectionOfReviews();
console.log(cor);
cor.add(feedback);
cor.add(feedback2);
console.log(cor);

for (let review of cor.reviews) {
    console.log(review.toString());
}

for (let review of cor) {
    console.log(`${review}`);
}