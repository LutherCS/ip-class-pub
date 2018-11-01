/* jshint esversion: 7 */
/* jshint node: true */
'use strict';

async function getData(url) {
    return fetch(url)
        .then(response => response.json())
        .catch(error => console.log(error));
}

async function getComments(postId) {
    let postComments = await getData(`http://jsonplaceholder.typicode.com/posts/${postId}/comments`);
    document.querySelector('#commCount' + postId ).innerHTML = postComments.length;
}
