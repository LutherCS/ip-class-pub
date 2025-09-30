"use strict";

class CollectionView {
    constructor(model) {
        model.subscribe(this.loadReviews.bind(this));
    }

    loadReviews(all_reviews, msg) {
        let allReviewsElement = document.querySelector("#reviewsDiv");
        allReviewsElement.innerHTML = "";

        for (let review of all_reviews) {
            // console.log(review.toString());

            let newReviewElement = document.createElement("p");
            newReviewElement.classList.add("box");
            newReviewElement.innerHTML = `<strong>${review.food.name}</strong><br>${review.opinion}`;

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

}