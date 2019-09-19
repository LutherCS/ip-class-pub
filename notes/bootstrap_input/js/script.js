/* jshint esversion: 6 */
/* jshint browser: true */
"use strict;";

const allCourses = {
    "Fundamentals of Web Programming": [130, 2],
    "Data Modeling and Querying": [140, 2],
    "Introduction to Computer Science": [150, 4],
    "Algorithms and Data Structures": [160, 4],
    "Object-Oriented Programming With Java": [252, 2],
    "Object-Oriented Programming With C++": [253, 2],
    "Computational Models": [260, 4],
    "Writing in the Major Lab": [296, 1],
    "Internet Programming": [330, 4],
    "Embedded Android Programming": [352, 2],
    "Embedded iOS Programming": [353, 2],
    "Advanced Algorithms and Data Structures": [360, 4],
    "Programming Languages": [370, 4],
    "Understanding Entrepreneurship in Silicon Valley": [385, 4],
    "The Digital Transformation of Central Europe": [386, 4],
    "Computer Networks": [430, 4],
    "Database Management Systems": [440, 4],
    "Operating Systems and Architecture": [450, 4],
    "Information Assurance and Security": [460, 4],
    "Senior Project I": [490, 2],
    "Senior Project II": [491, 2]
};

const gradePoints = {
    "A": 4.0,
    "A-": 3.7,
    "B+": 3.3,
    "B": 3.0,
    "B-": 2.7,
    "C+": 2.3,
    "C": 2.0,
    "C-": 1.7,
    "D+": 1.3,
    "D": 1.0,
    "D-": 0.7,
    "F": 0.0
};

function populateTitleOptions(titleSelect) {
    for (let course in allCourses) {
        let titleOption = document.createElement("option");
        titleOption.setAttribute("value", allCourses[course][0]);
        titleOption.innerText = course;
        titleSelect.appendChild(titleOption);
    }
    updateCredits(titleSelect.id, titleSelect.selectedOptions[0].innerHTML);
}

function populateGradeOptions(gradeSelect) {
    for (let grade in gradePoints) {
        let gradeOption = document.createElement("option");
        gradeOption.setAttribute("value", gradePoints[grade]);
        gradeOption.innerText = grade;
        gradeSelect.appendChild(gradeOption);
    }
}

function calculateGpa(buttonPressed=false) {
    let result = document.querySelector("#message");
    if (buttonPressed) {
        result.setAttribute("class", "alert alert-success text-center font-weight-bold");
    } else {
        result.setAttribute("class", "alert alert-warning text-center");
    }

    let coursesTaken = document.querySelectorAll("#grades > [class='row']");
    let gpa = 0;
    let cr_sum = 0;

    for (let course of coursesTaken) {
        let cr = parseInt(course.querySelector(".input_credits").value);
        let gp = course.querySelector(".select_grade").value;
        gpa += cr * gp;
        cr_sum += cr;
    }

    gpa = gpa / cr_sum;
    result.innerHTML = gpa.toFixed(2);
}

function updateCredits(courseId, courseTitle) {
    let currentCourse = parseInt(courseId.substring(5));
    let inputCredits = document.querySelector(`#credits${currentCourse}`);
    inputCredits.value = allCourses[courseTitle][1];
    calculateGpa();
}

function addCourse() {
    let allCourses = document.querySelector("#grades");
    let currentCourse = document.querySelectorAll("#grades > [class='row']").length + 1;
    let courseDiv = document.createElement("div");
    courseDiv.setAttribute("class", "row");

    let titleDiv = document.createElement("div");
    titleDiv.setAttribute("class", "form-group col-6");

    let titleDivLabel = document.createElement("label");
    titleDivLabel.setAttribute("for", `title${currentCourse}`);
    titleDivLabel.innerText = "Title";
    titleDiv.appendChild(titleDivLabel);

    let titleSelect = document.createElement("select");
    titleSelect.setAttribute("class", "form-control select_title");
    titleSelect.setAttribute("id", `title${currentCourse}`);
    titleSelect.setAttribute("onchange", "updateCredits(this.id, this.selectedOptions[0].innerHTML)");
    titleDiv.appendChild(titleSelect);

    courseDiv.appendChild(titleDiv);

    let creditsDiv = document.createElement("div");
    creditsDiv.setAttribute("class", "form-group col-3");

    let creditsDivLabel = document.createElement("label");
    creditsDivLabel.setAttribute("for", `credits${currentCourse}`);
    creditsDivLabel.innerText = "Credits";
    creditsDiv.appendChild(creditsDivLabel);

    let creditsInput = document.createElement("input");
    creditsInput.setAttribute("type", "number");
    creditsInput.setAttribute("class", "form-control input_credits");
    creditsInput.setAttribute("id", `credits${currentCourse}`);
    creditsInput.setAttribute("min", 0);
    creditsInput.disabled = true;
    creditsDiv.appendChild(creditsInput);
    courseDiv.appendChild(creditsDiv);

    let gradeDiv = document.createElement("div");
    gradeDiv.setAttribute("class", "form-group col-3");
    
    let gradeDivLabel = document.createElement("label");
    gradeDivLabel.setAttribute("for", `grade${currentCourse}`);
    gradeDivLabel.innerText = "Grade";
    gradeDiv.appendChild(gradeDivLabel);

    let gradeSelect = document.createElement("select");
    gradeSelect.setAttribute("class", "form-control select_grade");
    gradeSelect.setAttribute("id", `grade${currentCourse}`);
    gradeSelect.setAttribute("onchange", "calculateGpa()");
    gradeDiv.appendChild(gradeSelect);

    courseDiv.appendChild(gradeDiv);
    allCourses.appendChild(courseDiv);

    populateTitleOptions(titleSelect);
    populateGradeOptions(gradeSelect);
    calculateGpa();
}

$(document).ready(function () {
});