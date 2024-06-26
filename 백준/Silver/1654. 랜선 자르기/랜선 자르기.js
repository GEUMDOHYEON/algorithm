const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "JS/example.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [K, N] = input.shift().split(" ").map(Number);
const lines = input.map((a) => +a).sort();
let max = Math.max(...lines);
let min = 1;

while (max >= min) {
  let mid = parseInt((max + min) / 2);
  let count = lines
    .map((line) => parseInt(line / mid))
    .reduce((a, b) => a + b, 0);
  if (count < N) {
    max = mid - 1;
  } else {
    min = mid + 1;
  }
}
console.log(max);
