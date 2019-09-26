/* jshint esversion: 6 */
/* jshint node: true */
/* jshint browser: true */
/* jshint jquery: true */
"use strict";

class ClowderView {
    constructor(model) {
        model.subscribe(this.redrawList.bind(this));
    }

    redrawList(roster, msg) {
        let tblBody = document.querySelector("#rosterTable > tbody");
        tblBody.innerHTML = "";
        let tblHead = document.querySelector("#rosterTable > thead");
        if (roster.size > 0) {
            tblHead.setAttribute("style", "visibility: visible");
        } else {
            tblHead.setAttribute("style", "visibility: collapse");
        }
        for (let item of roster) {
            this.addRow(item, tblBody);
        }
    }

    addRow(cat, parent) {
        let row = document.createElement("tr");
        let cbCell = document.createElement("td");
        let cb = document.createElement("input");
        cb.type = "checkbox";
        cb.onclick = function() {
            cat.removed = !cat.removed;
        };
        cbCell.appendChild(cb);
        row.appendChild(cbCell);

        for (let val of ["name", "legs", "habitat", "diet"]) {
            let td = document.createElement("td");
            td.innerText = cat[val];
            row.appendChild(td);
        }
        parent.appendChild(row);
    }
}
