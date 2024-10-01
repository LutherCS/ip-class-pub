"use strict";

class TranscriptView {
    constructor(model) {
        model.subscribe(this.redrawView.bind(this));
    }

    redrawView(transcript, msg) {
        let tblBody = document.querySelector("#courses > tbody");
        tblBody.innerHTML = "";

        for (let course of transcript) {
            let row = document.createElement("tr");
            let tdTitle = document.createElement("td");
            tdTitle.innerHTML = course.title;
            row.appendChild(tdTitle);

            let tdCredits = document.createElement("td");
            tdCredits.innerHTML = course.credits;
            row.appendChild(tdCredits);

            let tdGrade = document.createElement("td");
            tdGrade.innerHTML = course.grade;
            row.appendChild(tdGrade);

            tblBody.appendChild(row);
        }
    }
}