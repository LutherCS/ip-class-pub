/* jshint esversion: 6 */
/* jshint node: true */
/* jshint browser: true */
/* jshint jquery: true */
"use strict";

function addGrade() {
    let roster = localStorage.getItem("storedRoster");
    roster = roster ? JSON.parse(roster) : [];
    let selMenuName = ["Name", "Major", "Grade"];

    let gradeItem = {};

    for (let cid of selMenuName) {
        gradeItem[cid] = document.getElementById(`sel${cid}`).value;
    }
    roster.push(gradeItem);
    localStorage.setItem("storedRoster", JSON.stringify(roster));

    console.log("Grade is added");
}

function showGrades() {
    let roster = localStorage.getItem("storedRoster");
    roster = roster ? JSON.parse(roster) : [];

    let displayDiv = document.querySelector("#roster");

    if (roster.length == 0) {
        displayDiv.innerHTML = "";
    }

    for (let student of roster) {
        let newRecord = document.createElement("div");
        newRecord.classList.add("alert");
        newRecord.classList.add("alert-primary");
        newRecord.innerHTML = `${student.Name} majoring in ${student.Major} earned ${student.Grade}`;
        displayDiv.appendChild(newRecord);
    }


    console.log("Grades are shown");
}

function clearGrades() {
    localStorage.clear();
    console.log("No more grades!");
}

$(document).ready(function() {
    showGrades();
});