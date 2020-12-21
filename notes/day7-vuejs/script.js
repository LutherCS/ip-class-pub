/* jshint esversion: 8 */
'use strict';

new Vue({
    el: "#app",
    data: {
        message: "Hello CS330",
        title: 'This page has been loaded on ' + new Date().toLocaleString()
    }
});

const inventory = new Vue({
    el: "#demo",
    data: {
        store: "Olin's Furniture",
        products: [
            {title: "Computer Mouse", price: Number.parseFloat(100).toFixed(2), quantity: 10},
            {title: "Computer Keyboard", price: Number.parseFloat(50).toFixed(2), quantity: 40},
            {title: "Computer Table", price: Number.parseFloat(1000).toFixed(2), quantity: 10},
            {title: "Computer Chair", price: Number.parseFloat(200).toFixed(2), quantity: 5},
        ],
    },
    computed: {
        totalValue() {
            return this.products.reduce((sum, product) => {
                return sum + product.price * product.quantity;
            }, 0).toFixed(2);
        }
    }
});
