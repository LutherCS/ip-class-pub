/* jshint esversion: 8 */
/* jshint node: true */
/* jshint browser: true */
'use strict';

class LabView {
    constructor(model) {
        model.subscribe(this.redrawList.bind(this));
    }

    redrawList(listOfMice, msg) {
        let tblBody = document.querySelector("#tblAllMice > tbody");
        tblBody.innerHTML = "";
        for (let mouse of listOfMice) {
            let row = document.createElement("tr");
            let tdButtons = document.createElement("td");
            tdButtons.innerHTML = mouse.buttons;
            row.appendChild(tdButtons);
            let tdConn = document.createElement("td");
            tdConn.innerHTML = mouse.connectionType;
            row.appendChild(tdConn);
            let tdColor = document.createElement("td");
            tdColor.innerHTML = mouse.color;
            row.appendChild(tdColor);
            tblBody.appendChild(row);
        }
    }
}


