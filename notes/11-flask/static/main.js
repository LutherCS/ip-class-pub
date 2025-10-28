"use strict";
/* Global constants */
const COLORS = { 1: "danger", 2: "warning", 3: "info", 4: "success" };
const REVIEWS = localStorage.getItem("fruitReviews") ? JSON.parse(localStorage.getItem("fruitReviews")) : [];

/**
 * Retrieve data from an API
 * @param {string} url
 * @returns JSON
 */
async function getData(url) {
  return fetch(url)
    .then(response => response.json())
    .catch(error => console.error(error));
}

/**
 * Collect data from the form and API and add a new review to the local storage
 */
async function saveReview() {
  /* Form validation */
  let isFormValid = true;
  let fruitName = document.querySelector("#fruitName").value;
  let fruitRating = "";
  let fruitOpinion = document.querySelector("#fruitOpinion").value;
  if (fruitName === "") {
    document.querySelector("#fruitNameHelp").classList.remove("is-hidden");
    isFormValid = false;
  } else {
    document.querySelector("#fruitNameHelp").classList.add("is-hidden");
  }
  try {
    fruitRating = parseInt(
      document.querySelector("input[name='fruit_rating']:checked").value
    );
    document.querySelector("#fruitRatingHelp").classList.add("is-hidden");
  } catch (e) {
    document.querySelector("#fruitRatingHelp").classList.remove("is-hidden");
    isFormValid = false;
  }
  if (isFormValid) {
    document.querySelector("#fruitName").value = "";
    document.querySelector("input[name='fruit_rating']:checked").checked = false;
    document.querySelector("#fruitOpinion").value = "";
  } else {
    return;
  }
  /* Data collection */
  const BASE_URL = "http://localhost:5000/api/fruit";
  let fruitData = await getData(`${BASE_URL}/${fruitName.toLowerCase()}`);
  if ("error" in fruitData) {
    fruitData = { nutritions: { "calories": "🤷", "carbohydrates": "🤷", "fat": "🤷", "protein": "🤷", "sugar": "🤷" } };
  }

  let newReview = {
    name: fruitName,
    rating: fruitRating,
    opinion: fruitOpinion,
    nutritions: fruitData.nutritions,
    date: new Date()
  }
  REVIEWS.push(newReview);
  localStorage.setItem("fruitReviews", JSON.stringify(REVIEWS));
  loadReviews();
}

/**
 * Delete a review
 * @param {Map} review
 */
function deleteReview(review) {
  REVIEWS.splice(REVIEWS.indexOf(review), 1);
  localStorage.setItem("fruitReviews", JSON.stringify(REVIEWS));
  loadReviews();
}

/**
 * Load reviews from local storage and display them all
 */
function loadReviews() {
  let allReviewsElement = document.querySelector("#allReviews");
  allReviewsElement.innerHTML = "";
  for (let review of REVIEWS) {
    let newReviewElement = document.createElement("div",);
    newReviewElement.classList.add("card");
    let color = COLORS[review.rating];
    newReviewElement.innerHTML = `
  <header class="card-header has-background-${color}">
    <p class="card-header-title">${review.name}</p>
    <button class="card-header-icon" aria-label="delete">
      <span class="delete icon">
      </span>
    </button>
  </header>
  <div class="card-content has-background-${color}-soft">${review.opinion}</div>
  <footer class="card-footer has-background-${color}">
  <p class="card-footer-item">Calories: ${review.nutritions.calories}</p>
  <p class="card-footer-item">Carbs: ${review.nutritions.carbohydrates}</p>
  <p class="card-footer-item">Fat: ${review.nutritions.fat}</p>
  <p class="card-footer-item">Protein: ${review.nutritions.protein}</p>
  <p class="card-footer-item">Sugar: ${review.nutritions.sugar}</p>
  </footer>
    `
    newReviewElement.querySelector("button").addEventListener("click", () => { deleteReview(review); });
    allReviewsElement.appendChild(newReviewElement);
  }
}

window.onload = function () {
  loadReviews();
}

document.querySelector("#submitReview").addEventListener("click", saveReview);