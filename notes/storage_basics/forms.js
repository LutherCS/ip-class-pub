/* jshint esversion: 6 */
/* jshint node: true */
'use strict';


function populateSelect(selectId, selectValues) {

}

function addMeal() {

}

function clearMenu() {

}

function loadMeal() {

}

$(document).ready(function () {
    populateSelect("sel_quantity", [2, 3, 5, 7]);
    populateSelect("sel_name", ['Apples', 'Bananas', 'Cookies']);
    populateSelect("sel_meal", ['Breakfast', 'Lunch', 'Dinner', 'Snack']);
    loadMeal();
});
