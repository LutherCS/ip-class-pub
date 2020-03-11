/* jshint esversion: 8 */
/* jshint node: true */
/* jshint jquery: true */
'use strict';

// fetch('https://jsonplaceholder.typicode.com/todos/1')
//   .then(response => response.json())
//   .then(json => console.log(json));

async function getData(url) {
    // return fetch(url, {mode: 'no-cors'})
    return fetch(url)
    .then(response => response.json())
    .catch(error => console.log(error));
}

async function populate() {
    let posts = await fetch("http://jsonplaceholder.typicode.com/posts")
    .then(response => response.json())
    .catch(error => console.log(error));

    let [users, comments] = await Promise.all([
        getData("http://jsonplaceholder.typicode.com/users"),
        getData("http://jsonplaceholder.typicode.com/comments")
    ]);

    let allPostsDiv = document.querySelector("#posts");

    for (let p of posts) {
        let p_id = p["id"];
        let p_user = p.user;
        let p_title = p.title;
        let p_body = p.body;
        
        let postDiv = document.createElement("div");
        postDiv.classList = "container border rounded mt-3";
        postDiv.innerHTML = p_body;
        allPostsDiv.appendChild(postDiv);
    }
}

$(document).ready(function() {
    populate();
});
