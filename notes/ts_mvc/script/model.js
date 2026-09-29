"use strict";
class Game {
    #title;
    #designer;
    #year;
    #review;
    constructor(title, designer, year, review) {
        this.#title = title;
        this.#designer = designer;
        this.#year = year;
        this.#review = review;
    }
    get title() {
        return this.#title;
    }
    get designer() {
        return this.#designer;
    }
    get year() {
        return this.#year;
    }
    get review() {
        return this.#review;
    }
    toString() {
        return `${this.#title} (${this.#year}) by ${this.#designer}`;
    }
    toJSON() {
        return {
            title: this.#title,
            designer: this.#designer,
            year: this.#year,
            review: this.#review,
        };
    }
}
class Shelf {
    #items;
    #handlers;
    constructor() {
        this.#items = [];
        this.#handlers = [];
    }
    subscribe(f) {
        this.#handlers.push(f);
    }
    publish(msg, obj) {
        for (let f of this.#handlers) {
            f(obj, msg);
        }
    }
    add(game) {
        this.#items.push(game);
        this.save(`${game.title} has been added`);
    }
    remove(game) {
        if (!this.#items.includes(game)) {
            throw new Error("Not found");
        }
        this.#items = this.#items.filter((item) => item != game);
        this.save(`${game.title} has been removed`);
    }
    save(message) {
        localStorage.setItem("myGames", JSON.stringify(this.#items));
        this.load(message);
    }
    load(message) {
        let localGames = localStorage.getItem("myGames");
        let parsedGames = localGames ? JSON.parse(localGames) : [];
        this.#items = [];
        for (let game of parsedGames) {
            this.#items.push(new Game(game.title, game.designer, game.year, game.review));
        }
        this.publish(message, this);
    }
    *[Symbol.iterator]() {
        for (let item of this.#items) {
            yield item;
        }
    }
}
