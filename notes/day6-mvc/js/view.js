/* jshint esversion: 8 */
/* jshint browser: true */
"use strict;";

class LabView {
    constructor(model) {
        // Connect to the model and redraw the table on change
        model.subscribe(this.redrawTable.bind(this));
    }

    redrawTable(listOfMice, msg) {
        let tblBody = document.querySelector("#tblAllMice > tbody");
        tblBody.innerHTML = "";

        for (let mouse of listOfMice) {
            let row = document.createElement("tr");
            let tdButtons = document.createElement("td");
            tdButtons.innerText = mouse.buttons;
            row.appendChild(tdButtons);
            
            let tdConnection = document.createElement("td");
            tdConnection.innerText = mouse.connectionType;
            row.appendChild(tdConnection);
            
            let tdColor = document.createElement("td");
            tdColor.innerText = mouse.color;
            row.appendChild(tdColor);

            tblBody.appendChild(row);
        }
    }
}