"use strict";

class Course {
    constructor(title, credits, grade) {
        this._title = title;
        this._credits = credits;
        this._grade = grade;
    }

    get title() {
        return this._title;
    }
    get credits() {
        return this._credits;
    }
    get grade() {
        return this._grade;
    }
}

class Subject {
    constructor() {
        this.handlers = [];
    }
    subscribe(func) {
        this.handlers.push(func);
    }

    publish(msg, obj) {
        let scope = obj || window;
        for (let f of this.handlers) {
            f(scope, msg);
        }
    }
}

class Transcript extends Subject {
    constructor() {
        super();
        this.transcript = [];
    }

    add(course) {
        this.transcript.push(course);
        this.publish("New course has been added", this);

    }

    calculateGPA() {
        let gpa = 0;
        let creditSum = 0;

        for (let course of this.transcript) {
            let cr = parseInt(course.credits);
            let gp = gradePoints[course.grade];

            gpa += cr * gp;
            creditSum += cr;
        }
        return gpa / creditSum;

    }

    [Symbol.iterator]() {
        let idx = -1;
        return {
            next: () => ({ value: this.transcript[++idx], done: !(idx in this.transcript) }),
        }
    }
}