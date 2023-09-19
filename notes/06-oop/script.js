"use strict";
console.log("JavaScript OOP");

// let a = 330;
// console.log(a);
// console.log(a++);
// console.log(++a);
// console.log(a);

class Vehicle {
    constructor(color, year, model) {
        this._color = color;
        this._year = year;
        this._model = model;
    }

    get color() {
        return this._color
    }

    set color(newValue) {
        this._color = newValue;
    }

    get year() {
        return this._year;
    }

    get model() {
        return this._model;
    }

    toString() {
        return `${this._color} ${this._year} ${this._model}`;
    }

    paint(newValue) {
        this._color = newValue;
    }
}

let v1 = new Vehicle();
console.log(v1);
console.log(v1._color);
v1._color = "norse blue";
console.log(v1._color);

let v2 = new Vehicle("pink", 2023, "Kaa");
console.log(v2);
console.log(v2.toString())

console.log("Setting the color");
v2.color = "lime";
console.log(v2.toString())
console.log("Setting the year");
try {
    v2.year = 2024

} catch (error) {
    console.log("Could not change the year");
}
console.log(v2.toString())
console.log("Painting the car");
v2.paint("black");
console.log(v2.toString())

class Garage {
    constructor() {
        this._allVehicles = [];
    }

    get vehicles() {
        return this._allVehicles;
    }

    buy(newVehicle) {
        this._allVehicles.push(newVehicle);
    }

    [Symbol.iterator]() {
        let idx = -1;
        return {
            next: () => ({ value: this._allVehicles[++idx], done: !(idx in this._allVehicles) })
        };
    }

}

console.log("My garage");
let g = new Garage()
g.buy(v1)
g.buy(v2)

console.log(g);
for (let v of g._allVehicles) {
    console.log(v.toString());
}

for (let v of g.vehicles) {
    console.log(v.toString());
}
for (let v of g) {
    console.log(v.toString());
}
