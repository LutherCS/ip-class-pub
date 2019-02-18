
/* jshint esversion: 6 */
/* jshint node: true */
'use strict';

var a_company = ["Frank", "Bob", "Alice", "Samuel"];
var adjectives = {"Frank": "exquisite", "Alice": "fine", "Bob": "not pleasant", "Samuel": "meh"};

var params = new URLSearchParams(window.location.search);

function sayHelloTed(name) {
    let the_name;
    if (name !== undefined) {
        the_name = name;
    } else {
        the_name = params.get("name");
    }
    let the_color = params.get("color");

    // sayHelloTed(the_color + " " + the_name);
    // document.write(`<span style="color: ${the_color}">${the_name}</span>`);
    document.querySelector("#visitor_name").innerHTML = `<span style="color: ${the_color}">${the_name}</span>`;
    // let all_p = document.querySelectorAll("p");
    // console.log(all_p.length);
    // for (let para of all_p) {
    //     console.log(para);
    //     para.innerHTML = "hohoho";
    //     let boo = document.createElement("span");
    //     boo.innerHTML = "whatever";
    //     para.appendChild(boo);
    // }
}

// function sayHelloTed(name) {
//     console.log(`Ted says hello to ${name}`);
// }

function greetCompany(many_people) {
    // for (let idx in many_people) {
    //     sayHelloTed(many_people[idx]);
    // }
    for (let person of many_people) {
        if (person === "Alice") {
            console.log("Hey, girl...");
        } else if (person === "Bob") {
            console.log("Oh, man...");
        } else {
            sayHelloTed(person);
        }
        console.log(`You are ${adjectives[person]} today`);
    }
}

// greetCompany(a_company);
