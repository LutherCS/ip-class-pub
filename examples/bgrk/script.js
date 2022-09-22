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


/**
 * Add a new game to the list
 * 
 */
function addGame() {
    let vals = [];
    let rowcolids = ["selTitle", "selDesigner", "selPublisher", "txtPrice", "datePurchased", "selRating"];
    for (let cid of rowcolids) {
        vals.push(document.getElementById(cid).value);
    }
    addRow(vals, document.querySelector("#myGames > tbody"));
}


/**
 * Add a new row to the table
 * 
 * @param {string[]} valueList list of task attributes
 * @param {Object} parent DOM node to append to
 */
function addRow(valueList, parent) {
    let row = document.createElement("tr");
    for (let val of valueList) {
        let td = document.createElement("td");
        td.innerHTML = val;
        row.appendChild(td);
    }
    parent.appendChild(row);
}

window.onload = function () {
    populateSelectorOptions("selTitle", "title");
    populateSelectorOptions("selDesigner", "designer");
    populateSelectorOptions("selPublisher", "publisher");
};