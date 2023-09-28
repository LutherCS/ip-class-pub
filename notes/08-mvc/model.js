"use strict";

class Shoe {
    constructor(brand, size, price) {
        this.brand = brand;
        this.size = size;
        this.price = price;
        this.quantity = 2;
    }
}

class Subject {
    constructor() {
        this.handlers = [];
    }
    subscribe(func) {
        this.handlers.push(func);
    }
    unsubscribe(func) {
        this.handlers = this.handlers.filter(item => item !== func);
    }
    publish(msg, obj) {
        let scope = obj || window;
        for (let f of this.handlers) {
            f(scope, msg);
        }
    }
}


class Footlocker extends Subject {
    constructor() {
        super();
        this.locker = [];
    }

    add(pair) {
        this.locker.push(pair);
        this.publish("New pair has been added", this);
    }

    remove(pair) { }

    clear() {
        this.locker = [];
        this.publish("Everything is gone", this);
    }

    [Symbol.iterator]() {
        let idx = -1;
        return {
            next: () => ({ value: this.locker[++idx], done: !(idx in this.locker) })
        };
    }
}
