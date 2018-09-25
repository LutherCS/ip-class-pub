/* jshint esversion: 6 */
/* jshint node: true */
'use strict';

var shoppingModel = new ShoppingList()

function clickedon() {
    let rowcolids = ['itemname', 'qty', 'store', 'category', 'price', 'priority'];
    let vals = {};
    for (let cid of rowcolids) {
        vals[cid] = document.getElementById(cid).value;
    }
    let it = new Item(vals.itemname, vals.qty, vals.priority, vals.store, vals.category, vals.price);
    shoppingModel.addItem(it);
}
