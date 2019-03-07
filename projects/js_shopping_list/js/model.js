/* jshint esversion: 6 */
/* jshint node: true */
'use strict';


class Item {
    // TODO: Implement the class
}


class Subject {
    constructor() {
        this.handlers = [];
    }

    subscribe(fn) {
        this.handlers.push(fn);
    }

    unsubscribe(fn) {
        this.handlers = this.handlers.filter(
            function(item) {
                if (item !== fn) {
                    return item;
                }
            }
        );
    }

    publish(msg, someObj) {
        var scope = someObj || window;
        for (let fn of this.handlers) {
            fn(scope, msg);
        }
    }
}


class ShoppingList extends Subject {
    // TODO: Implement the class
}


class LocalStorageSaver {
    // TODO: Implement the class
}
