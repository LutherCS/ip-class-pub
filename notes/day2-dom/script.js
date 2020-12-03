/* jshint esversion: 8 */

function addParagraph() {
    let contentDiv = document.querySelector("#content");
    let p = document.createElement("p");
    p.classList = "para";
    p.setAttribute("id", "third");
    p.innerText = "This is a new paragraph";
    contentDiv.append(p);
}

function greetByName() {
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    let greetElement = document.querySelector("h1");
    greetElement.innerHTML = `Hello ${urlParams.get('name')}`;
}

function setColor(newColor) {
    let theColor = newColor || "red" || "blue";
    let allParagraphs = document.querySelectorAll("p");
    for (let p of allParagraphs) {
        p.style = `color: ${theColor}`;
    }
}

window.onload = function () {
    addParagraph();
    this.greetByName();
    setColor();
};
