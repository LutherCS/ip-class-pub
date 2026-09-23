"use strict";

class Game {
    #title: string;
    #designer: string;
    #year: number;
    #price: number;

    constructor(title: string, designer: string, year: number) {
        this.#title = title;
        this.#designer = designer;
        this.#year = year;
        this.#price = 0;
    }
    get title() {return this.#title}
    get designer() {return this.#designer}
    get year() {return this.#year}
    get price() {return this.#price}
    set price(newPrice: number) {this.#price = newPrice;}


    toString() {
        return `${this.#title} was designed by ${this.#designer} in ${this.#year}`
    }
    toJSON() {
        return {"title": this.#title, "designer": this.#designer, "year": this.#year, "price": this.#price};
    }
}

class Shelf {
    #items: Array<Game>

    constructor() {
        this.#items = [];
    }

    add(game: Game) {
        this.#items.push(game);
    }

    remove(aGame: Game) {
        if (!this.#items.includes(aGame)) {
            throw new Error("Not found");
        }
        this.#items = this.#items.filter(item => item != aGame);
    }

    *[Symbol.iterator]() {
        for (let item of this.#items) {
            yield item;
        }
    }
}



let catan = new Game("Settlers of Catan", "Klaus Taube",1995)
console.log(catan.toString());
console.log(catan.year);
console.log(catan.price);
catan.price = 20.00;
console.log(catan.price);
console.log(catan.toJSON());
console.log(JSON.stringify(catan));

let myShelf = new Shelf();
myShelf.add(catan);
myShelf.add(new Game("UNO", "M Robbins", 1971));

for (let game of myShelf) {
    console.log(game.toString());
}
console.log("Removing Catan");

myShelf.remove(catan);
for (let game of myShelf) {
    console.log(game.toString());
}