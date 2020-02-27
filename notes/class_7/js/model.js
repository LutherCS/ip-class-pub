/* jshint esversion: 8 */
/* jshint node: true */
'use strict';

class ComputerMouse {
    constructor(nButtons, cType, color) {
        this._buttons = nButtons;
        this._connection = cType;
        this._color = color;
    }

    get buttons() {
        return this._buttons;
    }

    get connectionType() {
        return this._connection;
    }

    set connectionType(newValue) {
        this._connection = newValue;
    }

    get color() {
        return this._color;
    }

    set color(newValue) {
        this._color = newValue;
    }

    paint(newColor) {
        this._color = newColor;
    }

    toString() {
        return `A ${this._color} ${this._connection} mouse with ${this._buttons} buttons`;
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
        this.handlers = this.handlers.filter(item => item != func);
    }

    publish(msg, obj) {
        let scope = obj || window;
        for (let f of this.handlers) {
            f(scope, msg);
        }
    }
}

class Lab extends Subject {
    constructor(theSize) {
        super();
        this._size = theSize;
        this._lab = [];
    }

    add(mouse) {
        if (this._lab.length < this._size) {
            this._lab.push(mouse);
            this.publish("New mouse added", this);
        }
    }

    [Symbol.iterator]() {
        let idx = -1;
        return {
            next: () => ({value: this._lab[++idx], done: !(idx in this._lab)})
        };
    }
}
