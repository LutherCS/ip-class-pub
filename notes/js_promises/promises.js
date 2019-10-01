/* jshint esversion: 8 */
/* jshint node: true */
'use strict';

function resolve_with_wait() {
    return new Promise( resolve => {
        setTimeout(() => {
            resolve("resolved");
        }, 1000);
    });
}

async function f() {
    console.log("Calling resolve_with_wait");
    var result = await resolve_with_wait();
    console.log(result);
}

// f();
