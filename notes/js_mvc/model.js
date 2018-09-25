/* jshint esversion: 6 */
/* jshint node: true */
'use strict';

class Item {
    constructor(name, quantity, priority, store, section, price) {
        this.name = name;
        this.quantity = quantity;
        this.priority = priority;
        this.store = store;
        this.section = section;
        this.price = price;

        this._purchased = false;
    }
}

class ShoppingList {
    constructor() {
        this.newItems = [];
    }

    addItem(it) {
        this.newItems.push(it)
    }
}