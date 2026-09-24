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
    constructor() {
        this.#items = [];
    }
    add(game) {
        this.#items.push(game);
        this.save();
    }
    remove(aGame) {
        if (!this.#items.includes(aGame)) {
            throw new Error("Not found");
        }
        this.#items = this.#items.filter((item) => item != aGame);
        this.save();
    }
    save() {
        localStorage.setItem("myGames", JSON.stringify(this.#items));
        this.load();
    }
    load() {
        let localGames = localStorage.getItem("myGames");
        let parsedGames = localGames ? JSON.parse(localGames) : [];
        this.#items = [];
        for (let game of parsedGames) {
            this.#items.push(new Game(game.title, game.designer, game.year, game.review));
        }
        this.display();
    }
    display() {
        let allGames = document.querySelector("#allGames");
        allGames.innerHTML = "";
        for (let game of this.#items) {
            let gameInfo = document.createElement("p");
            gameInfo.classList.add("box");
            gameInfo.innerText = game.toString();
            allGames.appendChild(gameInfo);
        }
    }
    *[Symbol.iterator]() {
        for (let item of this.#items) {
            yield item;
        }
    }
}
var myShelf = new Shelf();
function addGame() {
    let title = document.querySelector("#titleInput").value;
    let designer = document.querySelector("#designerInput")
        .value;
    let year = parseInt(document.querySelector("#yearInput").value);
    let review = document.querySelector("#reviewInput")
        .value;
    let game = new Game(title, designer, year, review);
    myShelf.add(game);
}
window.onload = function () {
    document.querySelector("#addGameButton")?.addEventListener("click", addGame);
    myShelf.load();
};
