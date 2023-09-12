function paint(newColor) {
    let header = document.querySelector("h1");
    header.setAttribute("style", `color: ${newColor}`)
}

function takeNote() {
    let allNotesDiv = document.querySelector("#allNotes");
    let noteText = document.querySelector("#newNote");
    let newNote = document.createElement("p");
    newNote.innerText = noteText.value;
    newNote.class = "p";
    allNotesDiv.appendChild(newNote);
}