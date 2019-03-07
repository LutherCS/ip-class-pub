/* jshint esversion: 6 */
/* jshint node: true */
'use strict';

var stores = ["Ace Hardware", "Caseys", "Fareway", "Hatchery", "Walmart"];
var sections = ["Canned Goods", "Cereal", "Clothing", "Dairy", "Frozen Foods", "Liquor", "Meats", "Produce", "Tools"];
var quantities = [1, 2, 3, 4, 5, 10, 20, 30, 40, 50, 100];

var shoppingModel = new ShoppingList();
var shoppingView = new ShoppingView(shoppingModel);
var myDB = new LocalStorageSaver();



function clean_list() {
    // TODO: Remove all purchased items from the list and save it
}


function empty_list() {
    // TODO: Remove all items from the list and local storage
}


function save_list() {
    // TODO: Save the list to local storage
}


function populate_list() {
    // TODO: Read list from the local storage and add items to the model
}


function add_item() {
    // TODO: Collect values from HTML input fields, create a new Item, and add it to the model
}


function populateSelect(selectId, sList) {
    let sel = document.getElementById(selectId, sList);
    for (let s of sList) {
        let opt = document.createElement("option");
        opt.value = s;
        opt.innerHTML = s;
        sel.appendChild(opt);
    }
}


$(document).ready(function () {
    populateSelect("sel_quantity", quantities);
    populateSelect("sel_store", stores);
    populateSelect("sel_section", sections);
    populate_list();
});
