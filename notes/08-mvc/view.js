"use strict";

class FootlockerView {
    constructor(model) { }

    redrawView(footlocker, msg) {
        let tblBody = document.querySelector("#tbl_footlocket > tbody");
        tblBody.innerHTML = "";

        for (let pair of footlocker) {
            let row = document.createElement("tr");
            let tdBrand = document.createElement("td");
            tdBrand.innerText = pair.brand;
            row.appendChild(tdBrand);

            let tdSize = document.createElement("td");
            tdSize.innerText = pair.size;
            row.appendChild(tdSize);

            let tdPrice = document.createElement("td");
            tdPrice.innerText = pair.price;
            row.appendChild(tdPrice);

            tblBody.appendChild(tow);
        }
    }
}
