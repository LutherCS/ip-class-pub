/* jshint esversion: 8*/

function hello() {
    // console.log("Hello there!");
    let messagePara = document.querySelector("#message");
    messagePara.innerHTML = "Hello, <strong>CS330</strong>!";
}

function makeNewParagraph() {
    let containerDiv = document.querySelector("#container");
    let newPara = document.createElement("p");
    containerDiv.append(newPara);
    newPara.innerText = "This is a <em>new</em> paragraph";
}

function displayNumber(n) {
    let numberPara = document.querySelector("#message");
    numberPara.innerHTML = `The number is <strong>${n}</strong>`;
}