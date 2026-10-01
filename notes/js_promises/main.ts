"use strict";

import fruits from "./fruits.json" with { type: "json" };

function generateDataList(allFruits: Array<string>, listId: string) {
  let dataList = document.createElement("datalist");
  dataList.setAttribute("id", listId);
  for (let fruit of allFruits) {
    let opt = document.createElement("option");
    opt.value = fruit;
    dataList.appendChild(opt);
  }
  document.querySelector("body")?.appendChild(dataList);
}

async function getFruitData() {
  //   let baseUrl = "https://www.fruityvice.com/api/fruit/";
  let baseUrl = "https://wordsohard.com/api/v1/define/";
  let theFruit = (document.querySelector("#inCategory") as HTMLInputElement)
    .value;
  let targetUrl = `${baseUrl}${theFruit}`;
  let data = await fetch(targetUrl)
    .then((response) => response.json())
    .catch((e) => console.error(e));
  populateResult(data);
}

function populateResult(data: any) {
  let resultDiv = document.querySelector("#result");
  for (const def of data.definitions) {
    let p = document.createElement("p");
    p.innerHTML = def.definition;
    resultDiv?.appendChild(p);
  }
}

window.onload = function () {
  generateDataList(fruits, "data");
  document.querySelector("#btnAction")?.addEventListener("click", getFruitData);
};
