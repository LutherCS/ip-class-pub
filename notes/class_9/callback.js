/* jshint esversion: 8 */
/* jshint node: true */
'use strict';

function first() {
    return 1;
}

function second() {
    return 2;
}

// console.log(first());
// console.log(second);

function printWithTimeout() {
    setTimeout(function() {
        console.log(4);
    }, 500);
}

function printImmediately() {
    console.log(5);
}

// printWithTimeout();
// printImmediately();

function rudeAwakening() {
    console.log("And then I woke up");
}

function sleep(duration, f) {
    console.log(`I slept for ${duration} seconds`);
    f();
}

// sleep(5, rudeAwakening);
// sleep(3600, function() {console.log("And woke up happy");});

function doneSleeping() {
    let duration = 7;
    function reallyDone() {
        console.log(`I slept for ${duration} minutes`);
    }
    reallyDone();
}

// doneSleeping();
// reallyDone();

function done(activity) {
    return function() {
        console.log(`Done ${activity}`);
    };
}

// sleep(5, done("sleeping"));

var doneBound = function(activity) {
    console.log(`Done with ${activity}`);
};

// sleep(5, doneBound.bind(this, "sleeping"));

/** Naive approach */
// var counter = 0;

// function add1() {
//     counter++;
// }

// function rogueAdder() {
//     counter += 330;
// }

// console.log(counter);
// add1();
// rogueAdder();
// add1();
// console.log(counter);

var add1 = (function() {
    var counter = 0;
    return function() {counter += 1; return counter;};
})();

// console.log(add1());
// console.log(add1());
// console.log(add1());

function makeAdder(x) {
    return function (y) {
        console.log(`${x} + ${y} = ${x + y}`);
        return x + y;
    };
}

var add4 = makeAdder(4);
var add744 = makeAdder(744);

console.log(add4(330));
console.log(add744(330));

// twitter_object.get("search/tweets", params, function(err, data, response) {
//     if (!err) {
//         process(data)
//     }
// })