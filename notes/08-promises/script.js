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
    return fetch(url)
        .then(response => response.json())
        .catch(error => console.error(error));
}


/**
 * Get quote(s) for the chosen album
*/
async function getQuote() {
    let album = document.querySelector("#selAlbumTitle").value
    let number = document.querySelector("input[type='radio'][name='number']:checked").value;

    let url = "https://taylorswiftapi.onrender.com/get";
    if (number === "all") {
        url += "-all";
    }
    if (album != "Any") {
        url += `?album=${album}`;
    }
    let data = await getData(url);

    if (data.constructor == Object) { data = [data]; }

    let targetDiv = document.querySelector("#quotes");
    for (let quoteDict of data) {
        let nextQuote = document.createElement("div");
        nextQuote.classList.add("message");
        nextQuote.innerHTML = quoteDict.quote;
        targetDiv.appendChild(nextQuote);
    }

}

window.onload = function () {
    populateSelect("#selAlbumTitle", albums);
};