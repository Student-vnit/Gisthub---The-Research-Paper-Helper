const fetch = require('node-fetch');
const Blob = require('node-blob');
  var raw = "";

  var requestOptions = {
    method: 'POST',
    body: raw,
    redirect: 'follow'
  };
  
  fetch('https://gisthub-vnit.herokuapp.com/get_mp3?filename=r1.pdf',requestOptions)
  .then((response) => {
    // response.value for fetch streams is a Uint8Array
    var blob = new Blob([response.value], { type: 'audio/mp3' });
    var url = window.URL.createObjectURL(blob)
    window.audio = new Audio();
    window.audio.src = url;
    window.audio.play();
  })
  .catch((error) => {
    console.log(error);
  });