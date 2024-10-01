/* jshint node: true */
/* jshint esversion: 8 */
"use strict";

class Task{
    constructor(title, worker, priority, deadline) {
        this._title = title;
        this._worker = worker;
        this._priority = priority;
        this._deadline = deadline;
    }

    get title() {
        return this._title;
    }

    set title(newValue) {
        this._title = newValue;
    }

    get worker() {
        return this._worker;
    }

    set worker(newValue) {
        this._worker = newValue;
    }

    get priority() {
        return this._priority;
    }

    set priority(newValue) {
        this._priority = newValue;
    }

    get deadline() {
        return this._deadline;
    }

    set deadline(newValue) {
        this._deadline = newValue;
    }

    toString() {
        return `${this._worker} should ${this._title} by ${this._deadline}`;
    }

    daysLeft() {
        let today = new Date();
        let dueDate = Date.parse(this._deadline);
        return Math.ceil((dueDate - today) / (1000 * 60 * 60 * 24));
    }

}

let t = new Task("Record video", "Me", "Critical", "2020-12-10");
console.log(t.toString());
console.log(`The title of this tasks is ${t.title}`);
t.title = "Record video";
console.log(`The title of this tasks is ${t.title}`);
console.log(`This task is due in ${t.daysLeft()} day(s)`);

class TaskList {
    constructor() {
        this._allTasks = [];
    }

    add(newTask) {
        this._allTasks.push(newTask);
    }

    [Symbol.iterator]() {
        let index = -1;
        return {
            next: () => ({value: this._allTasks[++index], done: !(index in this._allTasks)})
        };
    }

}

let dailyTasks = new TaskList();
dailyTasks.add(t);
console.log(dailyTasks);
let anotherTask = new Task("Upload video", "Me", "Important", "2020-12-10");
dailyTasks.add(anotherTask);

console.log("All tasks for today");
for (let aTask of dailyTasks) {
    console.log(aTask.toString());
}
