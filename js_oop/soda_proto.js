/* jshint esversion: 6 */
/* jshint node: true */

'use strict';

function Can(radius, height) {
    this.radius = radius;
    this.height = height;
}

Can.prototype.volume = function() {
    return Math.PI * this.radius * this.radius * this.height;
};

let coke = new Can(2, 5);
console.log(coke.volume());

function Case() {
    this.case = [];
    for (let i = 0; i < 6; i++) {
        this.case.push(new Can(2, 5));
    }
}

let coke_case = new Case();

for (let i in coke_case.case) {
    console.log(i, coke_case.case[i].volume());
}
