#!/usr/bin/node
exports.converter = function (base) {
  return function (value) {
    return value.toString(base);
  };
};
