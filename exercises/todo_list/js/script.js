/* jshint esversion: 8 */
/* jshint browser: true */
"use strict;";

var team = ["Aardvark", "Beaver", "Cheetah", "Dolphin", "Elephant", "Flamingo", "Giraffe", "Hippo"];
var priority = ["Low", "Normal", "Important", "Critical"];

/**
 * Add a new task to the list
 * 
 * Validate form, collect input values, and add call `addRow` to add a new row to the table
 */
function addTask() {
    // TODO: Implement this function
    let vals = [];
    let rowcolids = ["title", "assignedTo", "priority", "dueDate"];

    addRow(vals, document.getElementById("taskList"));
}

/**
 * Add a new row to the table
 * 
 * @param {string[]} valueList list of task attributes
 * @param {Object} parent DOM node to append to
 */
function addRow(valueList, parent) {
    // TODO: Implement this function
    let row = document.createElement("tr");
    let td = document.createElement("td");
    let cb = document.createElement("input");

    parent.appendChild(row);
}

/**
 * Remove a table row corresponding to the selected checkbox
 * 
 * https://stackoverflow.com/questions/26512386/remove-current-row-tr-when-checkbox-is-checked
 */
function removeRow() {
    // TODO: Implement this function
}

/**
 * Remove all table rows
 * 
 */
function selectAll() {

}

/**
 * Add options to the specified element
 * 
 * @param {string} selectId `select` element to populate
 * @param {string[]} sList array of options
 */
function populateSelect(selectId, sList) {
    // TODO: Implement this function
    let sel = document.getElementById(selectId, sList);
}

window.onload = function () {
    populateSelect("assignedTo", team);
    populateSelect("priority", priority);
};
