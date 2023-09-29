#!/usr/bin/node

exports.esrever = function (list) {
  const i = list.slice(0);

  return i.reduceRight((ar, item) => (ar.push(item) ? ar : ar), []);
};
