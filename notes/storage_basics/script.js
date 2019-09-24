/* jshint esversion: 6 */
/* jshint node: true */
/* jshint browser: true */
/* jshint jquery: true */
'use strict';


function populateSelect(selectId, selectValues) {
    let sel = document.getElementById(selectId, selectValues);
    for (let s of selectValues) {
        let opt = document.createElement("option");
        opt.value = s;
        opt.innerHTML = s;
        sel.appendChild(opt);
    }
}

function addMeal() {
    let menu = localStorage.getItem("menu");
    menu = menu ? JSON.parse(menu) : [];
    let selNames = ["quantity", "name", "meal"];
    let newMeal = {};
    for (let cid of selNames) {
        newMeal[cid] = document.getElementById("sel_" + cid).value;
    }
    menu.push(newMeal);
    localStorage.setItem("menu", JSON.stringify(menu));
}

function clearMenu() {
    localStorage.removeItem("menu");
}

function loadMeal() {

}

$(document).ready(function () {
    populateSelect("sel_quantity", [2, 3, 5, 7]);
    populateSelect("sel_name", ['Apples', 'Bananas', 'Cookies']);
    populateSelect("sel_meal", ['Breakfast', 'Lunch', 'Dinner', 'Snack']);
    loadMeal();
});
