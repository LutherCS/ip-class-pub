"use strict";

class FootlockerView {
    constructor(model) {
        model.subscribe(this.redrawView.bind(this));
    }

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
            tdPrice.innerText = `$ ${Number.parseFloat(pair.price).toFixed(2)}`;
            row.appendChild(tdPrice);

            tblBody.appendChild(row);
        }
    }
}
