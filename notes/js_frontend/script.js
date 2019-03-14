/* jshint esversion: 6 */
"use strict";

const store = new Vue({
    el: "#storeName",
    data: {
        name: "Fareway",
        title: `Page loaded on ${new Date().toString()}`
    }
});

const list = new Vue({
    el: "#storeInventory",
    data: {
        products: [
            { name: "Milk", quantity: 3, price: 4.29 },
            { name: "Eggs", quantity: 5, price: 2.05 },
            { name: "Candy", quantity: 10, price: 1.99 }
        ]
    },
    computed: {
        stock() {
            return this.products.reduce((sum, product) => {
                return sum + product.quantity * product.price;
            }, 0).toFixed(2);
        }
    }
});
