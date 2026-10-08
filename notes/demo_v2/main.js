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
    toHTML() {
        return `
<article class="message is-info">
  <div class="message-header">
    ${this.toString()}
  </div>
  <div class="message-body">
    ${this.#review}
  </div>
</article>
`;
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
            let gameInfo = document.createElement("div");
            gameInfo.classList.add("p-2");
            gameInfo.innerHTML = game.toHTML();
            let deleteGame = document.createElement("button");
            deleteGame.classList.add("delete");
            deleteGame.addEventListener("click", function () {
                myShelf.remove(game);
            });
            gameInfo.querySelector("div.message-header")?.appendChild(deleteGame);
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
    const BASE_URL = "https://en.wikipedia.org/api/rest_v1/page/summary";
    let title = document.querySelector("#titleInput").value;
    if (title === "")
        return;
    const designerRE = /by [A-Z](\.|[\S]+)(\s[A-Z](\.|[\S]+))*/g;
    const yearRE = /in (\d\d\d\d)/g;
    getData(`${BASE_URL}/${title}_(board_game)`).then((data) => {
        const summary = data.extract;
        let designerGuess = summary.match(designerRE) ?? [
            "by Unknown",
        ];
        let yearGuess = summary.match(yearRE) ?? ["in 2026"];
        myShelf.add(new Game(title, designerGuess[0].substring(3), parseInt(yearGuess[0].substring(3)), summary));
    });
}
async function getData(url) {
    const myHeaders = new Headers();
    myHeaders.append("API-User-Agent", "GamelYY");
    return fetch(url, { headers: myHeaders })
        .then((response) => response.json())
        .catch((error) => console.log(error));
}
window.onload = function () {
    document.querySelector("#addGameButton")?.addEventListener("click", addGame);
    myShelf.load();
};
