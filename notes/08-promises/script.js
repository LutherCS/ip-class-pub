"use strict";

const albums = [
    "Taylor Swift",
    "Fearless",
    "Speak Now",
    "Red",
    "1989",
    "Reputation",
    "Lover",
    "Folklore",
    "Evermore",
    "Midnights",
    "The Tortured Poets Department",
]

/**
 * Populate select
 * @param {Selector idx} selectElementId 
 * @param {Options} options 
 */
function populateSelect(selectElementId, options) {
    let selectElement = document.querySelector(selectElementId);
    let defaultOption = document.createElement("option");
    defaultOption.innerHTML = "Any";
    selectElement.appendChild(defaultOption);
    for (let opt of options) {
        let optElem = document.createElement("option");
        optElem.innerHTML = opt;
        optElem.setAttribute("value", opt);
        selectElement.appendChild(optElem);
    }
}

/**
 * Retrieve data using fetch
 * @param {*} url 
 * @returns JSON
 */
async function getData(url) {

}


/**
 * Get quote(s) for the chosen album
*/
async function getQuote() {

}

window.onload = function () {
    populateSelect("#selAlbumTitle", albums);
};