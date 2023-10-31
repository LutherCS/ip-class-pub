'use strict;'

async function fetchData(url) {
    return fetch(url)
        .then(response => response.json())
        .catch(error => console.error(error));
}

async function getData(typeOfData) {
    let data = await fetchData(`http://localhost:5000/api/v1/${typeOfData}`);
    displayData(data["data"]);
}

function displayData(data) {
    let contentDiv = document.querySelector("#content");
    contentDiv.innerHTML = data;
}