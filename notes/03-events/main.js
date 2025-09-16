"use strict";

function paint(newColor) {
  let labelElement = document.querySelector("#ageLabel");
  //   labelElement.style.color = newColor;
  labelElement.setAttribute("style", `color: ${newColor}`);

  let ageInputElement = document.querySelector("#ageInput");
  if (newColor === "red") {
    ageInputElement.remove();
  }
}
