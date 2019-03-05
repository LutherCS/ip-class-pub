/* jshint esversion: 6 */
/* jshint node: true */
/* jshint browser: true */
/* jshint jquery: true */
"use strict";

class PlaylistView {
    constructor(model) {
        model.subscribe(this.redrawList.bind(this));
    }

    redrawList(playlist, msg) {
        console.log(msg);
        let plDiv = document.querySelector("#playlistDiv");
        let tbl = plDiv.querySelector("table");
        if (!tbl) {
            tbl = document.createElement("table");
            tbl.setAttribute("id", "playlistTable");
            plDiv.appendChild(tbl);
        }
        
        tbl.innerHTML = "";
        for (let song of playlist) {
            this.addRow(song, tbl);
        }
    }

    addRow(song, parent) {
        let row = document.createElement("tr");

        let cb = document.createElement("input");
        cb.type = "checkbox";
        cb.onclick = function() {
            song.removed = !song.removed;
        };
        let cbCell = document.createElement("td");
        cbCell.appendChild(cb);
        row.appendChild(cbCell);

        for (let val of ["title", "artist", "label", "album"]) {
            let td = document.createElement("td");
            td.innerText = song[val];
            row.appendChild(td);
        }

        parent.appendChild(row);
    }
}
