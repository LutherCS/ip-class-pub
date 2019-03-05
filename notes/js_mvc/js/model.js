/* jshint esversion: 6 */
/* jshint node: true */
"use strict";

class Song {
    constructor(title, artist, label, album) {
        this._title = title;
        this._artist = artist;
        this._label = label;
        this._album = album;

        this._removed = false;
    }

    get title() {
        return this._title;
    }

    get artist() {
        return this._artist;
    }

    get label() {
        return this._label;
    }

    get album() {
        return this._album;
    }

    get removed() {
        return this._removed;
    }

    set removed(newValue) {
        this._removed = newValue;
    }

    toString() {
        return `${this._title} (${this._album}) by ${this._artist} (${this._label})`;
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
        for (let func of this.handlers) {
            func(scope, msg);
        }
    }
}

class Playlist extends Subject {
    constructor() {
        super();
        this.allSongs = [];
    }

    add(aSong) {
        this.allSongs.push(aSong);
        this.publish("New song is added", this);
    }

    cleanList() {
        this.allSongs = this.allSongs.filter(aSong => !aSong.removed);
        this.publish("The list is cleaned up", this);
    }

    toString() {
        return `${this.allSongs}`;
    }

    get size() {
        return this.allSongs.length;
    }

    [Symbol.iterator]() {
        var idx = -1;
        return {
            next: () => ({value: this.allSongs[++idx], done: !(idx in this.allSongs)})
        };
    }
}
