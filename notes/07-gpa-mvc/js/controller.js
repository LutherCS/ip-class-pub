"use strict";

const allCourses = {
    "Fundamentals of Web Programming": 130,
    "Data Modeling and Querying": 140,
    "Introduction to Computer Science": 150,
    "Algorithms and Data Structures": 160,
    "Object-Oriented Programming With Java": 252,
    "Internet Programming": 330,
};

const gradePoints = {
    "A": 4.0,
    "B": 3.0,
    "C": 2.0,
    "D": 1.0,
    "F": 0.0,
};

function populateSelect(selectElementId, options) {
    let selectElement = document.querySelector(selectElementId);
    for (let opt in options) {
        let optElem = document.createElement("option");
        optElem.setAttribute("value", opt);
        optElem.innerHTML = opt;
        selectElement.appendChild(optElem);
    }
}

window.onload = function (params) {
    populateSelect("#courseTitle", allCourses);
    populateSelect("#courseGrade", gradePoints);
}