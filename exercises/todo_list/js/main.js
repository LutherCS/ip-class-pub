"use strict;";

var team = ["Aardvark", "Beaver", "Cheetah", "Dolphin", "Elephant", "Flamingo", "Giraffe", "Hippo"];
var priority = ["Low", "Normal", "Important", "Critical"];

/**
 * Add a new task to the list
 * 
 * Validate form, collect input values, and call `addRow` to add a new row to the table
 */
function addTask() {
    // TODO: Implement this function
    let vals = [];

    addRow(vals, document.querySelector("#taskList > tbody"));
}

/**
 * Add a new row to the table
 * 
 * Add each value as a separate cell
 * The first cell must be a checkbox to mark a task complete
 * 
 * @param {string[]} valueList list of task attributes
 * @param {Object} parent DOM node to append to
 */
function addRow(valueList, parent) {
    // TODO: Implement this function
    let row = document.createElement("tr");
    parent.appendChild(row);
}

/**
 * Remove a table row corresponding to the selected checkbox after a 2 second timeout
 * 
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
}

window.onload = function () {
    // Populate select elements automatically on page load
    populateSelect("assignedTo", team);
    populateSelect("priority", priority);
};
