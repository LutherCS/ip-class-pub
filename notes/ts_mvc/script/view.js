"use strict";
class ShelfView {
    constructor(model) {
        model.subscribe(this.display);
    }
    display(collection, message) {
        console.debug(`Updating the view because ${message}`);
        let allGames = document.querySelector("#allGames");
        allGames.innerHTML = "";
        for (let game of collection) {
            let gameInfo = document.createElement("div");
            gameInfo.classList.add("notification");
            gameInfo.innerText = game.toString();
            let btn = document.createElement("button");
            btn.classList.add("delete");
            btn.addEventListener("click", function () {
                collection.remove(game);
            });
            gameInfo.appendChild(btn);
            allGames.appendChild(gameInfo);
        }
    }
}
