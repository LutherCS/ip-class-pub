/* jshint esversion: 6 */
/* jshint node: true */
"use strict;";

console.log("Hello from the SeaWorld!");

class Lobster {
    constructor(color, age) {
        this.colorOfALobster = color;
        if (age < 0) {
            this.ageOfALobster = 0;
        } else {
            this.ageOfALobster = age;
        }
    }

    get color() {
        return this.colorOfALobster;
    }

    set color(new_value) {
        this.colorOfALobster = new_value;
    }

    get age() {
        return this.ageOfALobster;
    }

    set age(new_value) {
        console.error("Cannot change the age!");
    }

    getOlder() {
        this.ageOfALobster = this.ageOfALobster + 1;
    }

    join(some_pod) {
        some_pod.add(this);
    }

    toString() {
        return `This ${this.colorOfALobster} lobster is ${this.ageOfALobster} year(s) old`;
    }

}

function makeLobster() {
    let sammy = new Lobster("blue", 425);
    console.log(sammy.toString());
    sammy.color = "yellow";
    console.log(sammy.toString());
    sammy.age = 500;
    console.log(sammy.toString());
    for (let i = 0; i < 100; i++) {
        sammy.getOlder();
    }
    console.log(sammy.toString());

    let barb = new Lobster("green", -10);
    console.log(barb.toString());
    barb.color = "magenta";
    console.log(barb.toString());
}

// makeLobster();

class Pod {
    constructor() {
        this.ourPod = [];
        this.ageOfPod = 0;
        this.sizeOfPod = 0;
    }

    add(new_lobster) {
        this.ourPod.push(new_lobster);
        this.ageOfPod += new_lobster.age;
        this.sizeOfPod += 1;
    }

    toString() {
        return `Total age of ${this.sizeOfPod} lobsters is ${this.ageOfPod}`;
    }

    [Symbol.iterator]() {
        let idx = -1;
        return {
            next: () => ({value: this.ourPod[++idx], done: !(idx in this.ourPod)})
        };
    }
}

a_pod = new Pod();
console.log(a_pod.toString());

frank = new Lobster("red", 330);
a_pod.add(frank);
console.log(a_pod.toString());


funny = new Lobster("maroon", 370);
a_pod.add(funny);
console.log(a_pod.toString());

benny = new Lobster("silver", 100);
benny.join(a_pod);
console.log(a_pod.toString());

for (let a_lobster of a_pod) {
    console.log(a_lobster.toString());
}
