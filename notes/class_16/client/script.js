/* jshint esversion: 8 */
/* jshint node: true */
/* jshint browser: true */
'use strict'

const BASE_URL = "http://localhost:5000/api/v1"

async function requestData(typeOfData) {
    return fetch(`${BASE_URL}/${typeOfData}`)
    .then(response => response.json())
    .then(json => printData(json[typeOfData]))
    .catch(error => console.log(error))
}

function printData(data) {
    let responseDiv = document.querySelector("#response");
    responseDiv.innerHTML = data;
}
