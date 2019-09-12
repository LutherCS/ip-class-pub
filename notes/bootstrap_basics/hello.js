function boo() {
    let body = document.querySelector("body");
    let aaa = document.createElement("p");
    aaa.classList = "alert alert-warning";
    aaa.innerHTML = "Bye!";
    body.appendChild(aaa);
}

$(document).ready(function () {
    boo();
});