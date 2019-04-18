
"Use strict;"
"Jshint browser: true"
"Jshint node: true"
"Jshint esversion: 6"


async function getData(url){

    return fetch(url)
        .then(response => response.json())
        .catch(error => console.log(error));

}

async function getJoke(url){
    let response = await getData(url);
    let respDiv = document.getElementById("jokeHere");
    respDiv.innerHTML = response.joke;
}

async function getSpecificJoke(url){
    let id = document.getElementById("jokeNum").value;
    let response = await getData(url+"/"+id);
    let respDiv = document.getElementById("jokeHere");
    //respDiv.innerHTML = response.joke;
    respDiv.innerHTML = response.joke;
    
}
