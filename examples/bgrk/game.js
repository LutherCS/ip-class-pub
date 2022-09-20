/* jshint esversion: 8 */
/* jshint strict: true */
/* jshint node: true */
"use strict";

class Game {
    constructor(title, designer) {
        this._title = title;
        this._designer = designer;
    }

    get title() {
        return this._title;
    }

    set title(newValue) {
        this._title = newValue;
    }

    toString() {
        return `${this._title} by ${this._designer}`;
    }
}

class Library {
    constructor() {
        this._collection = [];
    }

    add(newGame) {
        this._collection.push(newGame);
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


let aGame = new Game("Pandemic", "Matt Leacock");
let bGame = new Game("Ticket to Ride", "Alan Moon");
console.log(aGame);
console.log(aGame.toString());
console.log(aGame._title);
console.log(aGame.title);
aGame.title = "Ticket to Ride";
console.log(aGame.title);
let myGames = new Library();
myGames.add(aGame);
myGames.add(bGame);
console.log(myGames);
console.log(`There are ${myGames.length} games in my collection`);
for (let game of myGames) {
    console.log(game.toString());
}
