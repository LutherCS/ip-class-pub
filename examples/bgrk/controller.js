/* jshint esversion: 8 */
/* jshint node: true */
/* jshint browser: true */
'use strict';

var myLibraryModel = new Library();
var myLibraryView = new LibraryView(myLibraryModel);

/**
 * Add a new game to the list
 * 
 */
function addGame() {
    let title = document.querySelector("#selTitle").value;
    let designer = document.querySelector("#selDesigner").value;
    let publisher = document.querySelector("#selPublisher").value;
    let price = document.querySelector("#txtPrice").value;
    let purchased = document.querySelector("#datePurchased").value;
    let rating = document.querySelector("#selRating").value;

    let newGame = new Game(title, designer, publisher, price, purchased, rating);
    console.log(`Controller just added ${newGame.toString()}`);
    myLibraryModel.add(newGame);
}
