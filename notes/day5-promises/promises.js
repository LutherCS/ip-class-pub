/* jshint esversion: 8 */
/* jshint node: true */
'use strict';

function resolve_with_wait() {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve("Promise resolved");
    }, 1000);
    });
}

function func() {
    console.log("Calling resolve_with_wait synchronously");
    let result = resolve_with_wait();
    console.log(result);
    console.log("Done");
}

func();

async function async_func() {
    console.log("Calling resolve_with_wait asynchronously");
    let result = await resolve_with_wait();
    console.log(result);
    console.log("Done");
}

async_func();
