console.log("Hello, CS330");
console.log(x);

var x = 330;
console.log(x);

const personName = "Timmy";
let personAge = 24;
console.log(personName + " is " + personAge);
// personName = "Timothee";
personAge++;
console.log(`${personName} is ${personAge}`);

if (personAge > 0) {
  console.log("Weclome to the world!");
} else {
  console.log("How did we make it here?");
}

for (let i = 0; i < 10; i++) {
  console.log(i);
}

let roster = ["Jon", "James", "Mike", "Michael"];
console.log(roster);
for (let i = 0; i < roster.length; i++) {
  console.log(roster[i]);
}

for (let name in roster) {
  console.log(name);
}

roster.push(11);
roster.push(4);
roster.push(42);
roster.push(10000000);
for (let name of roster) {
  console.log(name);
}
console.log(roster);
roster.sort();
console.log(roster);

let picks = [7, 21, 70, 9, 86];
picks.sort();
console.log(picks);
picks.sort((a, b) => a - b);
console.log(picks);

let grades = { Lucy: 90, Doug: 78 };
grades["Brad"] = 67;
grades.Douglas = 96;
console.log(grades);

console.log(greet(personName));

function greet(name) {
  return "Hello, " + name;
}

let oddStuff = [true, false, 1, 200, 10000];
oddStuff.sort();
console.log(oddStuff);

window.onload = function () {
  const urlParams = new URLSearchParams(window.location.search);
  let tableElement = document.querySelector("table > tbody");
  let newRow = document.createElement("tr");
  let newCountryCell = document.createElement("td");
  newCountryCell.innerHTML = urlParams.get("name");
  newRow.appendChild(newCountryCell);
  let newPopulationCell = document.createElement("td");
  newPopulationCell.innerHTML = urlParams.get("population");
  newRow.appendChild(newPopulationCell);
  tableElement.appendChild(newRow);
};
