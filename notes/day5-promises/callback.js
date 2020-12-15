/* jshint esversion: 6 */
/* jshint node: true */
'use strict';

/* Simple example */
/** simple function */
function first() {
    console.log(1);
}
/** simple function */
function second() {
    console.log(2);
}

// first();
// second();

/* Example with timeout */
/** simple function with timeout */
function firstWithWait() {
    setTimeout(function () {
        console.log(1);
    }, 500);
}

// firstWithWait();
// second();

/* Callback example */
/** eat calls back f */
function eat(food, f) {
    console.log(`Eating ${food}`);
    f();
}
// eat("veggies", first);

/* Defining function in place */
/** it's possitble to have an anonymous function*/
// eat("veggies", function() {
//     console.log("Done eating");
// });

/* Using a defined function */
/** simple function */
function doneEating() {
    console.log(`Done eating`);
}

// eat("more chikin", doneEating);

/* Lexical scoping */
/** insider has access to member variables of almostDone */
function almostDone() {
    let activity = "eating";
    let noun = "breakfast";
    function insider() {
        console.log(`Done ${activity} ${noun}`);
    }
    insider();
}

// almostDone();

/* Closure example */
/** simple closure */
function done(activity, noun) {
    return function () {
        console.log(`Done ${activity} ${noun}`);
    }
}

// eat("more chikin", done("eating", "chicken"));

/* Bind example */
var doneBind = function (activity, noun) {
    console.log(`Done ${activity} ${noun}`);
};

// eat("more chikin", doneBind.bind(this, "eating", "chicken"));

/* Closure with counter */
/** Naive approach */
// function add1() {
//     var counter = 0;
//     counter++;
// }

var add1 = (function () {
    var counter = 0;
    return function () { counter += 1; return counter }
})();

// console.log(add1());
// console.log(add1());
// console.log(add1());

/* Closure with adder */
/** adder factory */
function makeAdder(x) {
    return function (y) {
        console.log(`${x} + ${y} = ${x + y}`)
        return x + y;
    };
}

var add2 = makeAdder(2);
var add10 = makeAdder(10);

// console.log(add2);
// console.log(add2(5));
// console.log(add10(5));

/* Realistic  callback example */
// twitter_object.get('search/tweets', params, function(err, data, response) {
//     if(!err){
//       // This is where the magic will happen
//     } else {
//       console.log(err);
//     }
// })