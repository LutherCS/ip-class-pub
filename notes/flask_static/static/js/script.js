/* jshint esversion: 6 */
/* jshint node: true */
"use strict";

const hello = new Vue({
    el: "#vue_hello",
    delimiters: ["[[", "]]"],
    data: {
        vue_message: "Hello from Vue!"
    }
});
