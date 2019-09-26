/* jshint esversion: 6 */
/* jshint node: true */
/* jshint browser: true */
"use strict";

var allLegs = [0, 1, 2, 3, 4];
var allHabitats = ["kitchen", "basement", "attic"];

var myRosterModel = new Clowder();
var myClowderView = new ClowderView(myRosterModel);

function addCat() {
    if (!document.querySelector("#newCat").checkValidity()) {
        document.querySelector("#catName").setAttribute("style", "background-color: pink;");
        document.querySelector("#catDiet").setAttribute("style", "background-color: pink;");
        return;
    }
    document.querySelector("#catName").setAttribute("style", "background-color: white;");
    document.querySelector("#catDiet").setAttribute("style", "background-color: white;");

    let name = document.querySelector("#catName").value;
    let legs = document.querySelector("#catLegs").selectedOptions[0].value;
    let habitat = document.querySelector("#catHabitat").selectedOptions[0].value;
    let diet = document.querySelector("#catDiet").value;

    let newCat = new Cat(name, habitat, legs, diet);
    myRosterModel.adopt(newCat);

    if (myRosterModel.size === 1) {
        let cleanUpBtn = document.createElement("button");
        cleanUpBtn.setAttribute("type", "button");
        cleanUpBtn.setAttribute("id", "cleanBtn");
        cleanUpBtn.setAttribute("class", "btn btn-warning");
        cleanUpBtn.setAttribute("onclick", "cleanList()");
        cleanUpBtn.innerText = "Clean up the list";
        let body = document.querySelector("body");
        body.appendChild(cleanUpBtn);

    }
}

function cleanList() {
    myRosterModel.cleanList();
    if (myRosterModel.size == 0) {
        let cleanUpBtn = document.createElement("button");
        let body = document.querySelector("body");
        body.removeChild(cleanUpBtn);
    }
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
