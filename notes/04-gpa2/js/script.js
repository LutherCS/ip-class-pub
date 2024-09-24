"use strict;";

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

function addClass() {
    // Find the grades div
    let gradesDiv = document.querySelector("#grades");
    // Make a new class inputs
    let classDiv = document.createElement("div");
    classDiv.setAttribute("class", "columns");

    let currentClass = document.querySelectorAll("#grades > div").length + 1;

    let titleDiv = document.createElement("div");
    titleDiv.setAttribute("class", "column is-half");
    let titleSelect = document.createElement("select");
    titleSelect.setAttribute("class", "input select_title");
    titleSelect.setAttribute("id", `title${currentClass}`);
    titleDiv.appendChild(titleSelect);

    let creditsDiv = document.createElement("div");
    creditsDiv.setAttribute("class", "column");
    let creditInput = document.createElement("input");
    creditInput.setAttribute("type", "number");
    creditInput.setAttribute("class", "input input_credits");
    creditInput.setAttribute("min", 0);
    creditInput.setAttribute("id", `credits${currentClass}`);
    creditsDiv.appendChild(creditInput);

    let gradeDiv = document.createElement("div");
    gradeDiv.setAttribute("class", "column");
    let gradeSelect = document.createElement("select");
    gradeSelect.setAttribute("class", "input select_grade");
    gradeSelect.setAttribute("id", `grade${currentClass}`);
    gradeSelect.setAttribute("onchange", "calculateGPA()");
    gradeDiv.appendChild(gradeSelect);

    classDiv.appendChild(titleDiv);
    classDiv.appendChild(creditsDiv);
    classDiv.appendChild(gradeDiv);
    gradesDiv.appendChild(classDiv);

    populateSelect(titleSelect, allCourses);
    populateSelect(gradeSelect, gradePoints);
}

function populateSelect(selectElement, options) {
    for (let opt in options) {
        let anOption = document.createElement("option");
        anOption.setAttribute("value", options[opt]);
        anOption.innerHTML = opt;
        selectElement.appendChild(anOption);
    }

}

function calculateGPA() {
    let resultDiv = document.querySelector("#message");
    let courses = document.querySelectorAll("#grades > div");
    let gpa = 0;
    let creditSum = 0;

    for (let course of courses) {
        let cr = parseInt(course.querySelector(".input_credits").value);
        let gp = parseFloat(course.querySelector(".select_grade").value);

        gpa += cr * gp;
        creditSum += cr;
    }
    gpa = gpa / creditSum;
    resultDiv.innerHTML = gpa.toFixed(3);
}