#!/usr/bin/node
const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], (error, response, body) => {
    if (error) {
        console.error(error);
    } else {
        const film = JSON.parse(body);
        console.log(film.title);

        const characters = film.characters;
        const wedges = characters.filter((character) => character.match(/people\/18\//));
        console.log(wedges.length);
    }
});
