"use strict";

// const fruits = ["Apple", "Banana", "Cherry", "Durian"]
import jsonData from "./fruits.json" with {type: "json"};

/**
 * Use JSON to generate datalist
 * @param {*} json 
 */
function generateDatalist(json) {
  let fruitList = document.createElement("datalist");
  fruitList.setAttribute("id", "fruits");
  for (let fruit of json) {
    let opt = document.createElement("option");
    opt.value = fruit;
    fruitList.appendChild(opt);
  }
  document.body.appendChild(fruitList);
}

/**
 * Retrieve data from an API
 * @param {*} url 
 * @returns JSON
 */
async function getData(url) {
  return fetch(url)
    .then(response => response.json())
    .catch(error => console.error(error));
}

/**
 * Save review while translating its text
 * @returns 
 */
async function saveReview() {
  let BASE_URL = "https://api.funtranslations.com/translate/yoda.json?text";
  let fruitName = document.querySelector("#fruitName").value;
  let fruitReview = document.querySelector("#fruitReview").value;
  let fruitRating = "";
  if (fruitName === "") {
    return;
  }
  try {
    fruitRating = parseInt(
      document.querySelector("input[name='rating']:checked").value
    );
  } catch (e) {
    return;
  }
  document.querySelector("#fruitName").value = "";
  let fruitData = await fetch(`${BASE_URL}=${fruitReview}`).then(response => response.json());
  // The call to getData is 
  // let fruitData = await getData(`${BASE_URL}=${fruitReview}`);
  fruitReview = fruitData.contents.translated;

  let all_reviews = localStorage.getItem("all_reviews");
  if (all_reviews) {
    all_reviews = JSON.parse(all_reviews);
  } else {
    all_reviews = [];
  }
  let newReviewItem = {};
  newReviewItem.name = fruitName;
  newReviewItem.rating = fruitRating;
  newReviewItem.text = fruitReview;
  all_reviews.push(newReviewItem);
  localStorage.setItem("all_reviews", JSON.stringify(all_reviews));
  loadReviews();
}

function loadReviews() {
  let all_reviews = localStorage.getItem("all_reviews");
  all_reviews = all_reviews ? JSON.parse(all_reviews) : [];

  let allReviewsElement = document.querySelector("#reviewsDiv");
  allReviewsElement.innerHTML = "";
  for (let review of all_reviews) {
    let newReviewElement = document.createElement("p");
    newReviewElement.classList.add("box");
    newReviewElement.innerHTML = `<strong>${review.name}</strong><br>${review.text}`;

    switch (review.rating) {
      case 1:
        newReviewElement.classList.add("has-background-danger");
        break;
      case 2:
        newReviewElement.classList.add("has-background-warning-light");
        break;
      case 3:
        newReviewElement.classList.add("has-background-info");
        break;
      case 4:
        newReviewElement.classList.add("has-background-success");
        break;
    }
    allReviewsElement.appendChild(newReviewElement);
  }
}

window.onload = function () {
  loadReviews();
  generateDatalist(jsonData);
}

document.querySelector("#submitBtn").addEventListener("click", saveReview);