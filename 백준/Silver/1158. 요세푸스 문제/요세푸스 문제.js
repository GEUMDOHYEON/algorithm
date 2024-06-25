const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "JS/example.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [N, K] = input[0].split(" ").map(Number);
const q = Array.from({ length: N }, (_, i) => i + 1);
const result = [];
let count = 1;

while (q.length) {
  const tmp = q.shift();
  if (count % K === 0) {
    result.push(tmp);
  } else {
    q.push(tmp);
  }
  count += 1;
}

console.log(`<${result.join(", ")}>`);
