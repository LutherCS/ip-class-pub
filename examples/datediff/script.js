"use strict;"

function diff() {
    let d1 = new Date(document.querySelector("#date1").value);
    let d2 = new Date(document.querySelector("#date2").value);
    let dd = Math.abs((d2 - d1) / (1000 * 60 * 60 * 24));

    let tbl = document.querySelector("#result > tbody");
    let newRow = document.createElement("tr");
    let td1 = document.createElement("td");
    td1.innerText = d1.toLocaleDateString();
    newRow.appendChild(td1);

    let td2 = document.createElement("td");
    td2.innerText = d2.toLocaleDateString();
    newRow.appendChild(td2);

    let td3 = document.createElement("td");
    td3.innerText = dd;
    newRow.appendChild(td3);

    tbl.appendChild(newRow);
}
