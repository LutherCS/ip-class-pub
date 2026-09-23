"use strict";

class Game {
    constructor(title, designer, year) {
        this.title = title;
        this.designer = designer;
        this.year = year;
    }

    toString() {
        return `${this.title} was designed by ${this.designer} in ${this.year}`
    }
}


class Shelf {
    constructor() {
        this.items = [];
    }

    add(newTitle) {
        this.items.push(newTitle);
    }

    *[Symbol.iterator]() {
        for (let item of this.items) {
            yield item;
        }
    }
}

let risk = new Game("Risk", "Albert Lamorisse", 1957);
console.log(risk);
console.log(risk.title);
let monopoly = new Game("Landlord", "Elizabeth Magie", 1904)
console.log(monopoly.toString());

let myGames = new Shelf();
myGames.add(risk);
myGames.add(monopoly);
console.log(myGames)

risk.title = "RISK!!!"
risk.time = "Forever"
risk.year = [1, 2, 3]
for (let game of myGames) {
    console.log(game.toString());
    // console.log(game);
}