function greetUser() {
    const queryStr = window.location.search;
    const urlParams = new URLSearchParams(queryStr);
    // console.log(queryStr);
    console.log(urlParams);
    let name = urlParams.get("name");
    let greetingElement = document.querySelector("h1#greeting");
    greetingElement.innerHTML = `Greetings, <strong>${name}</strong>`;

    let mainElem = document.querySelector("main");
    let age = urlParams.get("age") || 3;
    for (let i = 0; i < age; i++) {
        let newParagraph = document.createElement("p");
        newParagraph.innerHTML = `Hello, <strong>${name}</strong>`;
        mainElem.appendChild(newParagraph);
    }

}

function changeColor(newColor) {
    let greetingElement = document.querySelector("h1#greeting");
    greetingElement.style.color = newColor;
    // Change the color of the name
    let name = document.querySelector("h1#greeting > strong");
    name.style.color = newColor;
}

function cleanUp() {
    let allParagraphs = document.querySelectorAll("main > p");
    for (let elem of allParagraphs) {
        elem.remove();
    }
}

window.onload = function () {
    // console.log("Made it here!");
    this.greetUser();
}