/* jshint esversion: 6 */
/* jshint node: true */
'use strict';


class ShoppingView {
    constructor(model) {
        // The bind() method creates a new function that, when called, has its this keyword set to the provided value.
        model.subscribe(this.redrawList.bind(this));
    }

    redrawList(shoppingList, msg) {
        // TODO: Redraw the table, include all the items from the model
    }

    addRow(item, parent) {
        // TODO: Add a row with item description to the table
    }
}
