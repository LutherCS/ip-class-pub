/* jshint esversion: 6 */
/* jshint node: true */
/* jshint browser: true */
"use strict";

var myPlayList = new Playlist();

function clickedon() {
    let title = document.querySelector("#songTitle").value;
    let artist = document.querySelector("#songArtist").selectedOptions[0].value;
    let label = document.querySelector("#songLabel").selectedOptions[0].value;
    let album = document.querySelector("#songAlbum").value;
    let newSong = new Song(title, artist, label, album);

    console.log(newSong.toString());
}






