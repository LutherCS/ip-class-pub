/* jshint esversion: 6 */
/* jshint browser: true */
"use strict;";

var team = ["Aardvark", "Beaver", "Cheetah", "Dolphin", "Elephant", "Flamingo", "Giraffe", "Hippo"];
var priority = ["Low", "Normal", "Important", "Critical"];

function addTask() {
    /* Collect valid values from the input fields and call addRow() to add a row to the table of tasks */
}

function addRow(valueList, parent) {
    /* Create a new row element with data provided in the valueList and append this row to the table (parent) provided */
}

function removeRow() {
    /* Remove the row of the table is a checkbox in that row is clicked (checked) */
}

function populateSelect(selectId, sList) {
    /* Populate the option (drop-down) element (selectId) with items from the sList */
}

window.onload = function () {
    populateSelect("assignedTo", team);
    populateSelect("priority", priority);
};
