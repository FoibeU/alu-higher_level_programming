#!/usr/bin/node
$(document).ready(() => {
    $.get('https://fourtonfish.com/hellosalut/?lang=fr', (data) => {
      $('#hello').text(data.hello);
    });
  });