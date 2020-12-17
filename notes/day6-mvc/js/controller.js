/* jshint esversion: 8 */
/* jshint browser: true */
"use strict;";

const connectionTypes = ["wired", "bluetooth", "infrared"];
const colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

var myLabModel = new ComputerLab(10);
var myLabView = new LabView(myLabModel);

function populateSelect(selectElement, options) {
    for (let opt of options) {
        let anOption = document.createElement("option");
        anOption.setAttribute("value", opt);
        anOption.innerHTML = opt;
        selectElement.appendChild(anOption);
    }

}

function addMouse() {
    if (!document.querySelector("#newMouse").checkValidity()) {
        let warning = document.createElement("p");
        warning.setAttribute("class", "alert alert-warning");
        warning.innerText = "Enter all values please";
        document.querySelector("body").appendChild(warning);
        return;
    }

    let buttons = document.querySelector("#mouseButtons").value;
    let connectionType = document.querySelector("#mouseConnection").selectedOptions[0].value;
    let color = document.querySelector("#mouseColor").selectedOptions[0].value;

    // Add to the model
    let newMouse = new ComputerMouse(buttons, connectionType, color);
    myLabModel.add(newMouse);
}

window.onload = function() {
    populateSelect(document.querySelector("#mouseConnection"), connectionTypes);
    populateSelect(document.querySelector("#mouseColor"), colors);
};
