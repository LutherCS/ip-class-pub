/* jshint esversion: 6 */
/* jshint browser: true */
/* jshint jquery: true */
/* jshint node: true */
"use strict";

async function getData(url) {
    return fetch(url)
    .then(response => response.json())
    .catch(error => console.log(error));
}

async function populate() {
    console.log("Loading...");
    let [posts, users] = await Promise.all([
        getData("https://jsonplaceholder.typicode.com/posts"),
        getData("https://jsonplaceholder.typicode.com/users")
    ]);
    console.log("Done loading data.");
    // console.log(posts);
    // console.log(users);
    let allPostsDiv = document.querySelector("#posts");
    for (let post of posts) {
        let postDiv = document.createElement("div");
        postDiv.classList.add("container", "border", "border-dark", "rounded", "mt-1");
        
        let headDiv = document.createElement("div");
        headDiv.classList.add("row");
        postDiv.appendChild(headDiv);

        let titleDiv = document.createElement("div");
        titleDiv.classList.add("col", "h5");
        titleDiv.innerHTML = post["title"];
        headDiv.appendChild(titleDiv);

        let userDiv = document.createElement("div");
        userDiv.classList.add("col", "h5");
        let userId = post["userId"];
        userDiv.innerHTML = users[userId - 1]["name"];
        headDiv.appendChild(userDiv);

        let commCount = document.createElement("div");
        commCount.classList.add("col");
        let postId = post["id"];
        let postComments = await getData(`https://jsonplaceholder.typicode.com/posts/${postId}/comments`);
        commCount.innerHTML = postComments.length;
        headDiv.appendChild(commCount);

        let bodyDiv = document.createElement("div");
        bodyDiv.classList.add("row");
        bodyDiv.innerHTML = post["body"];
        postDiv.appendChild(bodyDiv);

        allPostsDiv.appendChild(postDiv);
    }

}

$(document).ready(function() {
    populate();
});
