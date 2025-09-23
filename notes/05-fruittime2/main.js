function saveReview() {
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
}