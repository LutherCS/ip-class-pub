/* jshint esversion: 8 */
/* jshint node: true */
/* jshint browser: true */
'use strict';

var allGames = [
    { "title": "Settlers of Catan", "designer": "Klaus Teuber", "publisher": "Kosmos" },
    { "title": "Pandemic", "designer": "Matt Leacock", "publisher": "Z-Man Games" },
    { "title": "Ticket to Ride", "designer": "Alan R. Moon", "publisher": "Days of Wonder" },
];

/**
 * Populate a selector with options
 * 
 * @param {String} selectorID id of the `select` to populate with options
 * @param {String} optionName name of the option
 */

function populateSelectorOptions(selectorID, optionName) {
    let selectorElement = document.querySelector(`#${selectorID}`);
    for (let game of allGames) {
        let optElement = document.createElement("option");
        optElement.value = game[optionName];
        optElement.innerText = game[optionName];
        selectorElement.appendChild(optElement);
    }
}

class LibraryView {
    constructor(model) {
        model.subscribe(this.redrawTable.bind(this));
    }

    redrawTable(listOfGames) {
        let tblBody = document.querySelector("#myGames > tbody");
        tblBody.innerHTML = "";

        for (let game of listOfGames) {
            let row = document.createElement("tr");

            let cellTitle = document.createElement("td");
            cellTitle.innerText = game.title;
            row.appendChild(cellTitle);

            let cellDesigner = document.createElement("td");
            cellDesigner.innerText = game.designer;
            row.appendChild(cellDesigner);

            let cellPublisher = document.createElement("td");
            cellPublisher.innerText = game.publisher;
            row.appendChild(cellPublisher);

            let cellPrice = document.createElement("td");
            cellPrice.innerText = `$ ${Number(game.price).toFixed(2)}`;
            row.appendChild(cellPrice);

            let cellPurchased = document.createElement("td");
            cellPurchased.innerText = new Date(game.purchased).toDateString();
            row.appendChild(cellPurchased);

            let cellRating = document.createElement("td");
            cellRating.innerText = "★".repeat(Number(game.rating));
            row.appendChild(cellRating);

            console.log(`View just added ${game.toString()}`);
            tblBody.appendChild(row);
        }
    }
}

window.onload = function () {
    populateSelectorOptions("selTitle", "title");
    populateSelectorOptions("selDesigner", "designer");
    populateSelectorOptions("selPublisher", "publisher");
};