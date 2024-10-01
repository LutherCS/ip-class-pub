/* jshint esversion: 8 */
/* jshint browser: true */
/* jshint node: true */
/* jshint jquery: true */
'use strict';

function populateSelect(selectElement, options) {
    for (let opt of options) {
        let anOption = document.createElement("option");
        anOption.setAttribute("value", opt);
        anOption.innerHTML = opt;
        selectElement.appendChild(anOption);
    }
}

function addCar() {
    let garage = localStorage.getItem("local_garage");
    garage = garage ? JSON.parse(garage) : [];
    let selNames = ["make", "model", "year"];
    let newCar = {};
    for (let i of selNames) {
        newCar[i] = document.querySelector(`#sel_${i}`).value;
    }
    garage.push(newCar);
    localStorage.setItem("local_garage", JSON.stringify(garage));
    loadCars();
}

function loadCars() {
    let garage = localStorage.getItem("local_garage");
    garage = garage ? JSON.parse(garage) : [];
    let garageDiv = document.querySelector("#garage");
    garageDiv.innerHTML = "";

    for (let car of garage) {
        let carAlert = document.createElement("div");
        carAlert.classList = "alert alert-primary";
        carAlert.innerHTML = `${car.make} ${car.model} (${car.year})`;
        garageDiv.appendChild(carAlert);
    }
}

function clearAll() {
    localStorage.removeItem("local_garage");
}

$(document).ready(function(){
    populateSelect(document.querySelector("#sel_make"), ["Audi", "BMW", "Chevy"]);
    populateSelect(document.querySelector("#sel_model"), ["Matrix", "Santa Fe", "1500"]);
    populateSelect(document.querySelector("#sel_year"), ["2019", "2020", "2021"]);
    loadCars();
});
