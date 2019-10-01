/* jshint esversion: 8 */
/* jshint node: true */
/* jshint browser: true */
/* jshint jquery: true */
'use strict';

async function populate() {
    // let data = await getData("https://jsonplaceholder.typicode.com/posts");
    // console.log(data);
    let [posts, users, comments] = await Promise.all([
        getData("https://jsonplaceholder.typicode.com/posts"),
        getData("https://jsonplaceholder.typicode.com/users"),
        getData("https://jsonplaceholder.typicode.com/comments"),
    ]);

    console.log(posts);
    // console.log(users);
    // console.log(comments);
    let postsDiv = document.querySelector("#posts");
    for (let post of posts) {
        let p = document.createElement("p");
        p.innerText = post.body;
        postsDiv.appendChild(p);

    }
}

async function getData(url) {
    return fetch(url)
        .then(response => response.json())
        .catch(error => console.log(error));
}

$(document).ready(function () {
    populate();
});
