"use strict";

var myShelf = new Shelf();
var myShelfView = new ShelfView(myShelf);

function addGame() {
  let title = (document.querySelector("#titleInput") as HTMLInputElement).value;
  let designer = (document.querySelector("#designerInput") as HTMLInputElement)
    .value;
  let year = parseInt(
    (document.querySelector("#yearInput") as HTMLInputElement).value,
  );
  let review = (document.querySelector("#reviewInput") as HTMLInputElement)
    .value;
  let game = new Game(title, designer, year, review);
  myShelf.add(game);
}

window.onload = function () {
  document.querySelector("#addGameButton")?.addEventListener("click", addGame);
  myShelf.load("Initialization is complete");
};
