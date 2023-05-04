#!/usr/bin/node

const request = require('request');
const id = process.argv[2];

request('https://swapi-api.alx-tools.com/api/films/' + id, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  } else {
    const data = JSON.parse(body).characters;
    for (const character of data) {
      request(character, function (error, response, body) {
        if (error) {
          console.log(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
