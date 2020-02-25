/* jshint esversion: 6 */
/* jshint browser: true */
"use strict;";

var team = ["Aardvark", "Beaver", "Cheetah", "Dolphin", "Elephant", "Flamingo", "Giraffe", "Hippo"];
var priority = ["Low", "Normal", "Important", "Critical"];

function addTask() {
}

function addRow(valueList, parent) {
}

function removeRow() {
    // https://stackoverflow.com/questions/26512386/remove-current-row-tr-when-checkbox-is-checked
}

function populateSelect(selectId, sList) {
}

window.onload = function() {
    populateSelect("assignedTo", team);
    populateSelect("priority", priority);
};
