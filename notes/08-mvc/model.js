"use strict";

class Shoe {
    constructor(brand, size, price) {
        this.brand = brand;
        this.size = size;
        this.price = price;
        this.quantity = 2;
    }
}

class Footlocker {
    constructor() {
        this.locker = [];
    }

    add(pair) {
        this.locker.push(pair);
    }

    remove(pair) { }

    [Symbol.iterator]() {
        let idx = -1;
        return {
            next: () => ({ value: this.locker[++idx], done: !(idx in this.locker) })
        };
    }
}
