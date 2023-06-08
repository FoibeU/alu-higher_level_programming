#!/usr/bin/node
const add = (a, b) => {
  const res = Number(a) + Number(b);
  console.log(res);
};

const n1 = process.argv[2];
const n2 = process.argv[3];

add(n1, n2);
