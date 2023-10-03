"use strict";

/**
 * Populate select
 * @param {Selector idx} selectElementId 
 * @param {Options} options 
 */
function populateSelect(selectElementId, options) {
    let selectElement = document.querySelector(selectElementId);
    for (let opt in options) {
        let optElem = document.createElement("option");
        optElem.innerHTML = opt;
        optElem.setAttribute("value", options[opt]);
        selectElement.appendChild(optElem);
    }
}

async function getData(url) {
    return fetch(url)
        .then(response => response.json())
        .catch(error => console.log(error));
}

async function getQuote() {
    let targetDiv = document.querySelector("#allQuotes");
    targetDiv.innerHTML = "";
    let series = document.querySelector("#sel_series").value;
    let number = parseInt(document.querySelector("#sel_number").value);
    let url = `https://${series}-quotes.vercel.app/api/quotes/${number}`;
    let data = await getData(url);
    // console.log(data);
    for (let a_quote of data) {
        // a_quote is a dictionary with 2 keys: quote and author
        let quoteP = document.createElement("p");
        quoteP.classList = "p";
        quoteP.innerHTML = a_quote.quote;
        quoteP.title = a_quote.author;
        targetDiv.appendChild(quoteP);
    }
}

window.onload = function () {
    populateSelect("#sel_series", { "Stranger Things": "strangerthings", "Lucifer": "lucifer", "Better Call Saul": "bcs" })
}