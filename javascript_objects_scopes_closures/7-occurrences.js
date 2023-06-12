#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let number = 0;
  list.forEach(element => {
    if (element === searchElement) {
      number += 1;
    }
  });
  return number;
};
