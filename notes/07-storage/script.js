"use strict";

function populateSelect(selectElementId, options) {
    let selectElement = document.querySelector(selectElementId);
    for (let opt of options) {
        let optElem = document.createElement("option");
        optElem.setAttribute("value", opt);
        optElem.innerHTML = opt;
        selectElement.appendChild(optElem);
    }

}

function addOutfit() {
    let closet = localStorage.getItem("myCloset");
    closet = closet ? JSON.parse(closet) : [];
    let selNames = ["brand", "type", "year"];
    let newOutfit = {};
    for (let name of selNames) {
        newOutfit[name] = document.querySelector(`#sel_${name}`).value;
    }
    closet.push(newOutfit);
    localStorage.setItem("myCloset", JSON.stringify(closet));
    loadOutfits();
}

function loadOutfits() {
    let closet = localStorage.getItem("myCloset");
    closet = closet ? JSON.parse(closet) : [];
    let closetDiv = document.querySelector("#closet");
    closetDiv.innerHTML = "";
    for (let outfit of closet) {
        let outfitDiv = document.createElement("div");
        outfitDiv.classList = "alert alert-primary";
        outfitDiv.innerHTML = `${outfit.type} by ${outfit.brand}`;
        closetDiv.appendChild(outfitDiv);
    }
}

function clearAll() {
    localStorage.removeItem("myCloset");
    loadOutfits();
}

window.onload = function (params) {
    populateSelect("#sel_brand", ["Nike", "Dior", "Gap"]);
    populateSelect("#sel_type", ["Shorts", "Hoodie", "Pants"]);
    populateSelect("#sel_year", [2023, 2022, 2021, 2020])
}