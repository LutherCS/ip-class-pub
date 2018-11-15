/* jshint esversion: 6 */
/* jshint node: true */
"use strict";

const app = new Vue({
    el: "#app",
    data: {
        message: "Fareway stock management"
    }
});

const demo = new Vue({
    el: "#store-demo",
    data: {
        products: [
            {name: "Apple", price: 7.00.toFixed(2), quantity: 20 },
            {name: "Banana", price: 0.11.toFixed(2), quantity: 2 },
            {name: "Cheerios", price: 4.99.toFixed(2), quantity: 8 },
        ]
    },
    computed: {
        stock() {
            return this.products.reduce((sum, product) => {
                return sum + product.quantity;
            }, 0)
        }
    }
});
