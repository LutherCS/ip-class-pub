/* jshint esversion: 6 */
/* jshint node: true */
/* jshint browser: true */
"use strict";

var allArtists = ["Aardvark", "Beaver", "Cheetah"];
var allLabels = ["Luther College", "Music Hits", "Golden Records"];

var myPlaylistModel = new Playlist();
var myPlaylistView = new PlaylistView(myPlaylistModel);

function addSong() {
    if (!document.querySelector("#newSongForm").checkValidity()) {
        document.querySelector("#songTitle").setAttribute("style", "background-color: pink;");
        document.querySelector("#songAlbum").setAttribute("style", "background-color: pink;");
        return;
    }
    let title = document.querySelector("#songTitle").value;
    let artist = document.querySelector("#songArtist").selectedOptions[0].value;
    let label = document.querySelector("#songLabel").selectedOptions[0].value;
    let album = document.querySelector("#songAlbum").value;
    let newSong = new Song(title, artist, label, album);

    myPlaylistModel.add(newSong);
}

function cleanList() {
    myPlaylistModel.cleanList();
}

function populateSelectOption(elementId, optionsArray) {
    let menu = document.querySelector(elementId);
    for (let artist of optionsArray) {
        let newOption = document.createElement("option");
        newOption.setAttribute("value", artist);
        newOption.innerHTML = artist;
        menu.appendChild(newOption);
    }
}

window.onload = function() {
    populateSelectOption("#songArtist", allArtists);
    populateSelectOption("#songLabel", allLabels);
};

