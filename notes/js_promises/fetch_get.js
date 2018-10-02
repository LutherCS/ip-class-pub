/* jshint esversion: 6 */
/* jshint node: true */
'use strict';


async function getData(url) {
    return fetch(url)
        .then(response => response.json())
        // .then(json => console.log(json))
        .catch(error => console.log(error));
}

async function populate() {
    let [posts, users] = await Promise.all([
        getData('https://jsonplaceholder.typicode.com/posts'),
        getData('https://jsonplaceholder.typicode.com/users')
    ]);

    // console.log(posts);
    // console.log(users);
    let postsDiv = document.querySelector('#posts');

    for (let post of posts) {
        let postId = post.id;
        let postTitle = post.title;
        let postBody = post.body;
        // console.log(postTitle);

        let postDiv = document.createElement('div');
        postDiv.classList.add('container', 'border', 'border-dark', 'rounded', 'mt-3');
        
        let postHead = document.createElement('div');
        postHead.classList.add('row');
        
        let postTitleDiv = document.createElement('div');
        postTitleDiv.classList.add('col', 'h5');
        postTitleDiv.innerHTML = post.title;
        postHead.appendChild(postTitleDiv);
        
        let userDiv = document.createElement('div');
        userDiv.classList.add('col', 'h5');
        let userId = post.userId;
        userDiv.innerHTML = users[userId-1]['name'];
        postHead.appendChild(userDiv);
        
        let commCountDiv = document.createElement('div');
        commCountDiv.classList.add('col');

        if (!('commsCount' in post)) {
            let postComments = await getData(`https://jsonplaceholder.typicode.com/posts/${postId}/comments`);
            post.commsCount = postComments.length;
        }
        commCountDiv.innerHTML = post.commsCount;

        postHead.appendChild(commCountDiv);

        postDiv.appendChild(postHead);
        
        let postBodyDiv = document.createElement('div');
        postBodyDiv.classList.add('row', 'p-1');
        postBodyDiv.innerHTML = post.body;
        
        postDiv.appendChild(postBodyDiv);

        postsDiv.appendChild(postDiv);
    }

}

$(document).ready(function () {
    populate();
});
