/* jshint esversion: 6 */
/* jshint browser: true */
/* jshint node: true */
"use strict";

async function getData(url) {
    return fetch(url)
    .then(response => response.json())
    .catch(error => console.log(error));
}

async function getName() {
    let response = await getData("http://localhost:5000/api/v1/names");
    printValue(response.name, "#response");
}

async function getAddress() {
    let response = await getData("http://localhost:5000/api/v1/addresses");
    printValue(response.address, "#response");

}

async function getSentence() {
    let response = await getData("http://localhost:5000/api/v1/sentences");
    printValue(response.sentence, "#response");

}

function printValue(value, divId) {
    let respDiv = document.querySelector(divId);
    respDiv.innerHTML = value;
}
