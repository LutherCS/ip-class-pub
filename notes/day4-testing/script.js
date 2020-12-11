/* jshint esversion: 8 */
/* jshint browser: true */
"use strict";

function paint(the_color) {
    let header = document.querySelector("h1");
    header.setAttribute("style", `color: ${the_color}`);
}

function takeNote() {
    let allNotesDiv = document.querySelector("#allNotes");
    let newNoteText = document.querySelector("#newNote").value;
    let p = document.createElement("p");
    let today = new Date();
    p.innerText = `${today}: ${newNoteText}`;
    p.classList = "p";
    allNotesDiv.append(p);
}
