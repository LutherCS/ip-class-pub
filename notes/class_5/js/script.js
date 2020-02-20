/* jshint esversion: 8 */
/* jshint node: true */
/* jshint browser: true */
'use strict';

var allCourses = {
    "Fundamentals of Web Programming": [130, 2],
    "Data Modeling and Querying": [140, 2],
    "Introduction to Computer Science": [150, 4]
};

var allGrades = {
    "A": 4.0,
    "B": 3.0,
    "C": 2.0,
    "D": 1.0,
    "F": 0
};

function populateTitleOption(titleSelect) {
    for (const course in allCourses) {
        let titleOption = document.createElement("option");
        titleOption.setAttribute("value", allCourses[course][0]);
        titleOption.innerHTML = course;
        titleSelect.appendChild(titleOption);
    }
}

function populateGradeOption(gradeSelect) {
    for (const grade in allGrades) {
        let gradeOption = document.createElement("option");
        gradeOption.setAttribute("value", allGrades[grade]);
        gradeOption.innerHTML = grade;
        gradeSelect.appendChild(gradeOption);
    }
}

function calculateGPA() {
    let alert_box = document.querySelector("#thegpa");
    alert_box.innerHTML = "you clicked the button";
}

function help() {
    let alert_box = document.querySelector("#thegpa");
    alert_box.innerHTML = "See notes/bootstrap_input for complete example";
}

function addGrade() {
    let allMyCourses = document.querySelector("#grades");
    let currentCourse = document.querySelectorAll("#grades > [class='row']").length + 1;
    let thisCourseDiv = document.createElement("div");
    thisCourseDiv.setAttribute("class", "row");

    let titleDiv = document.createElement("div");
    titleDiv.setAttribute("class", "form-group-col");

    let titleSelect = document.createElement("select");
    titleSelect.setAttribute("class", "form-control select_title");
    titleSelect.setAttribute("id", `title${currentCourse}`);

    let creditsDiv = document.createElement("div");
    creditsDiv.setAttribute("class", "form-group col-3");

    let creditsInput = document.createElement("input");
    creditsInput.setAttribute("type", "number");
    creditsInput.setAttribute("min", 0);

    creditsDiv.appendChild(creditsInput);

    populateTitleOption(titleSelect);
    titleDiv.appendChild(titleSelect);
    thisCourseDiv.appendChild(titleDiv);
    thisCourseDiv.appendChild(creditsDiv);
    allMyCourses.appendChild(thisCourseDiv);
}
