"use strict";

class ShelfView {
  constructor(model: Shelf) {
    model.subscribe(this.display);
  }
  display(collection: Shelf, message: string) {
    console.debug(`Updating the view because ${message}`);

    let allGames = document.querySelector("#allGames") as HTMLElement;
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
