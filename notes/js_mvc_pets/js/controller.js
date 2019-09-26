/* jshint esversion: 6 */
/* jshint node: true */
/* jshint browser: true */
"use strict";

var allLegs = [0, 1, 2, 3, 4];
var allHabitats = ["kitchen", "basement", "attic"];

var myRosterModel = new Clowder();
var myClowderView = new ClowderView(myRosterModel);

function addCat() {
    /* TODO */
}

function cleanList() {
    /* TODO */
}

function populateSelectOption(elementId, optionsArray) {
    let menu = document.querySelector(elementId);
    for (let artist of optionsArray) {
        let newOption = document.createElement("option");
        newOption.setAttribute("value", artist);
        newOption.innerHTML = artist;
        menu.appendChild(newOption);
    }
}

window.onload = function () {
    populateSelectOption("#catLegs", allLegs);
    populateSelectOption("#catHabitat", allHabitats);
};
