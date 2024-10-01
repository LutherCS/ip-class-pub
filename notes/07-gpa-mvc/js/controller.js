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

var myTranscriptModel = new Transcript();
var myTranscriptView = new TranscriptView(myTranscriptModel);

function populateSelect(selectElementId, options) {
    let selectElement = document.querySelector(selectElementId);
    for (let opt in options) {
        let optElem = document.createElement("option");
        optElem.setAttribute("value", opt);
        optElem.innerHTML = opt;
        selectElement.appendChild(optElem);
    }
}

function addCourse() {
    let title = document.querySelector("#courseTitle").selectedOptions[0].value;
    let credits = parseInt(document.querySelector("#courseCredits").value);
    let grade = document.querySelector("#courseGrade").value;

    myTranscriptModel.add(new Course(title, credits, grade));
}

function calculateGPA() {
    let gpa = myTranscriptModel.calculateGPA();
    let resultDiv = document.querySelector("#message");
    resultDiv.innerHTML = gpa.toFixed(3);
}

window.onload = function () {
    populateSelect("#courseTitle", allCourses);
    populateSelect("#courseGrade", gradePoints);
}