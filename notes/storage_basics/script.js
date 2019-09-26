/* jshint esversion: 6 */
/* jshint node: true */
/* jshint browser: true */
/* jshint jquery: true */
'use strict';


function populateSelect(selectId, selectValues) {
    let sel = document.getElementById(selectId, selectValues);
    for (let s of selectValues) {
        let opt = document.createElement("option");
        opt.value = s;
        opt.innerHTML = s;
        sel.appendChild(opt);
    }
}

function addMeal() {
    let menu = localStorage.getItem("menu");
    menu = menu ? JSON.parse(menu) : [];
    let selNames = ["quantity", "name", "meal"];
    let newMeal = {};
    for (let cid of selNames) {
        newMeal[cid] = document.getElementById("sel_" + cid).value;
    }
    menu.push(newMeal);
    localStorage.setItem("menu", JSON.stringify(menu));
}

function clearMenu() {
    localStorage.removeItem("menu");
}

function loadMeal() {
    let vals = JSON.parse(localStorage.getItem('menu'));
    let menu = document.querySelector('#menu');

    if (vals) {
        for (let meal of vals) {
            let menuItem = document.createElement('div');
            menuItem.classList.add('alert');
            menuItem.classList.add('alert-primary');
            menuItem.innerHTML += `You are having ${meal.quantity} ${meal.name} for ${meal.meal}`;
            menu.appendChild(menuItem);
        }
    } else {
        let banner = document.createElement('div');
        banner.classList.add('alert');
        banner.classList.add('alert-info');
        banner.innerHTML = 'Please select from the menu';
        menu.appendChild(banner);
    }
}

$(document).ready(function () {
    populateSelect("sel_quantity", [2, 3, 5, 7]);
    populateSelect("sel_name", ['Apples', 'Bananas', 'Cookies']);
    populateSelect("sel_meal", ['Breakfast', 'Lunch', 'Dinner', 'Snack']);
    loadMeal();
});
