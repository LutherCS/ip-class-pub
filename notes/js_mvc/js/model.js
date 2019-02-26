/* jshint esversion: 6 */
/* jshint node: true */
"use strict";

class Song {
    constructor(title, artist, label, album) {
        this._title = title;
        this._artist = artist;
        this._label = label;
        this._album = album;
    }

    get title() {
        return this._title;
    }

    toString() {
        return `${this._title} (${this._album}) by ${this._artist} (${this._label})`;
    }
}

class Playlist {
    constructor() {
        this.allSongs = [];
    }

    add(aSong) {
        this.allSongs.push(aSong);
    }
}