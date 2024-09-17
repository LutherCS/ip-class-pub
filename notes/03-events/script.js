function paint(newColor) {
    let header = document.querySelector("h1");
    header.setAttribute("style", `color: ${newColor}`);
    header.innerText = "Hello, students";
}