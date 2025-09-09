function greetName() {
  const queryStr = window.location.search;
  const urlParams = new URLSearchParams(queryStr);
  let greetingElement = document.querySelector("#grrrr");
  greetingElement.innerHTML = "Hello, " + urlParams.get("name");
}

window.onload = function () {
  greetName();
};
