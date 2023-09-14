function takeNote() {
    let allNotesDiv = document.querySelector("#allNotes");
    let noteText = document.querySelector("#newNoteText");
    if (noteText.value === "") {
        return;
    }
    let newNote = document.createElement("p");
    newNote.classList.add("border");
    let now = new Date();
    newNote.innerText = `${now.toLocaleString()}\n${noteText.value}`;
    let importance = document.querySelector("input[name='btnradio']:checked").value;
    switch (importance) {
        case "high":
            newNote.classList.add("text-danger");
            break;
        case "medium":
            newNote.classList.add("text-secondary");
            break;
        case "low":
            newNote.classList.add("text-success");
            break;
    }
    allNotesDiv.appendChild(newNote);
    document.querySelector("#newNoteText").value = "";
}