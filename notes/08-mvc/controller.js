"use strict";

var myFootlockerModel = new Footlocker();
var myFootlockerView = new FootlockerView(myFootlockerModel);

/**
 * Populate select
 * @param {Selector idx} selectElementId 
 * @param {Options} options 
 */
function populateSelect(selectElementId, options) {
    let selectElement = document.querySelector(selectElementId);
    for (let opt of options) {
        let optElem = document.createElement("option");
        optElem.setAttribute("value", opt);
        optElem.innerHTML = opt;
        selectElement.appendChild(optElem);
    }
}

/**
 * Add a pair of shoes to the footlocker
 * @returns if the form is invalid
 */
function addPair() {
    if (!document.querySelector("#shoe_details").checkValidity()) {
        return;
    }
    let brand = document.querySelector("#sel_brand").selectedOptions[0].value;
    let size = document.querySelector("#num_size").value;
    let price = document.querySelector("#num_price").value;
    let newPair = new Shoe(brand, size, price);
    myFootlockerModel.add(newPair);
}

function clearAll() {
    myFootlockerModel.clear();
}

window.onload = function (params) {
    populateSelect("#sel_brand", ["Adidas", "Nike", "Reebok", "Puma"]);
}