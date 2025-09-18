function saveReview() {
  let fruitName = document.querySelector("#fruitName").value;
  let fruiReview = document.querySelector("#fruitReview").value;
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
  let newReview = document.createElement("p");
  newReview.classList.add("box");
  newReview.innerHTML = `<strong>${fruitName}</strong><br>${fruiReview}`;

  switch (fruitRating) {
    case 1:
      newReview.classList.add("has-background-danger");
      break;
    case 2:
      newReview.classList.add("has-background-warning-light");
      break;
    case 3:
      newReview.classList.add("has-background-info");
      break;
    case 4:
      newReview.classList.add("has-background-success");
      break;
  }
  let allReviews = document.querySelector("#reviewsDiv");
  allReviews.appendChild(newReview);
  document.querySelector("#fruitName").value = "";
}
