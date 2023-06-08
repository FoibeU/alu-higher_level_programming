#!/usr/bin/node
const args = process.argv.slice(2);
const val = args.map(argnew => parseInt(argnew));

if (val.length === 0) {
  console.log(0);
} else if (val.length === 1) {
  console.log(0);
} else {
  const sortedval = val.sort((a, b) => b - a);
  console.log(sortedval[1]);
}
