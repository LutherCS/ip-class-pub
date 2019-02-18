
/* jshint esversion: 6 */
/* jshint node: true */
'use strict';

var params = new URLSearchParams(window.location.search);

function sayHello() {
    let name = params.get("name");
    document.write(`Hello ${name}`);
}
