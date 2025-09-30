"use strict";

var corModel = new CollectionOfReviews();
var corView = new CollectionView(corModel);

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

    let newFruit = new Fruit(fruitName, true);
    let newReview = new Review(newFruit, fruitRating, fruitReview);
    corModel.add(newReview);
}
