console.log("Made it this far")

function greetByName() {
    const queryStr = window.location.search
    const urlParams = new URLSearchParams(queryStr)
    let greetElement = document.querySelector("h1")
    greetElement.innerText = `Hello, ${urlParams.get('name')}`
}

window.onload = function () {
    this.greetByName();
}
