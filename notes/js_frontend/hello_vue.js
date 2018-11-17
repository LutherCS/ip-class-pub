/* jshint esversion: 6 */
/* jshint node: true */
"use strict";

const app = new Vue({
    el: "#app",
    data: {
        message: "FarFar away stock management"
    }
});

const demo = new Vue({
    el: "#store-demo",
    data: {
        products: [
            {name: "Apple", price: 7.00, quantity: 20 },
            {name: "Banana", price: 0.11, quantity: 2 },
            {name: "Cheerios", price: 4.99, quantity: 8 },
        ]
    },
    computed: {
        stock() {
            return this.products.reduce((sum, product) => {
                if (product.quantity > 0)
                    return sum + product.quantity;
                else
                    return sum;
            }, 0)
        }
    }
});
