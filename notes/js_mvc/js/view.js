/* jshint esversion: 6 */
/* jshint node: true */
/* jshint browser: true */
/* jshint jquery: true */
"use strict";

var allArtists = ["Aardvark", "Beaver", "Cheetah"];
var allLabels = ["Luther College", "Music Hits", "Golden Records"];

function populateSelectOption(elementId, optionsArray) {
    let menu = document.querySelector(elementId);
    for (let artist of optionsArray) {
        let newOption = document.createElement("option");
        newOption.setAttribute("value", artist);
        newOption.innerHTML = artist;
        menu.appendChild(newOption);
    }
}

window.onload = function() {
    populateSelectOption("#songArtist", allArtists);
    populateSelectOption("#songLabel", allLabels);
};
