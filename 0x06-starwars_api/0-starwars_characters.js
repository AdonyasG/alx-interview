#!/usr/bin/node

const request = require('request');
const id = process.argv[2];

request('https://swapi-api.alx-tools.com/api/films/' + id, async function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  }
  const data = JSON.parse(body).characters;
  for (const character of data) {
    await new Promise((resolve, reject) => {
      request(character, (error, response, body) => {
        if (error) {
          console.log(error);
        }
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
