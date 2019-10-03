"use strict";

const hello = new Vue({
    el: "#hello",
    data: {
        message: "Hello CS330",
        title: "This is some title"
    }
});

const inventory = new Vue({
    el: "#store-demo",
    data: {
        store: "Roman's Grocery Store",
        products: [
            {title: "Apple(s)", quantity: 3, price: Number.parseFloat(0.75).toFixed(2), origin: "Ukraine"},
            {title: "Banana(s)", quantity: 5, price: Number.parseFloat(0.15).toFixed(2), origin: "Georgia"},
            {title: "Candy bar(s)", quantity: 10, price: Number.parseFloat(1).toFixed(2), origin: "USA"},
        ]
    },
    computed: {
        stock_value() {
            return this.products.reduce((sum, product) => {
                return sum + product.price * product.quantity;
            }, 0).toFixed(2);
        }
    }
});
