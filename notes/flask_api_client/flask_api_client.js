"use strict";

function add() {
    let num1 = document.querySelector('#txt_num1').value;
    let num2 = document.querySelector('#txt_num2').value;
    let num3 = document.querySelector('#txt_num3').value;
    let num4 = document.querySelector('#txt_num4').value;

    let server_url = 'http://localhost:5000'
    fetch(`${server_url}/add?num1=${num1}&num2=${num2}`)
    .then(function(response) {
        return response.json();
    })
    .then(function(response) {
        document.querySelector('#result').innerHTML = response.result;
    })
    .catch(error => console.error('Error: ' + error));
}