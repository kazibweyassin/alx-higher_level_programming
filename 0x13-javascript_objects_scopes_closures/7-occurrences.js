#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  let i = 0;
  for (i of list) {
    if (i === searchElement) {
      count = count + 1;
    }
  }
  return count;
};
