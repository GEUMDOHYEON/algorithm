const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "JS/example.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [N, K] = input[0].split(" ").map(Number);
const visited = Array.from({ length: 100100 }, () => 0);

function bfs(N) {
  const q = [];
  q.push([N, 0]);
  visited[N] = 1;

  while (q.length) {
    const [cur, time] = q.shift();
    if (cur === K) {
      console.log(time);
      return;
    }
    for (next of [cur * 2, cur - 1, cur + 1]) {
      if (next >= 0 && next <= 100000 && !visited[next]) {
        visited[next] = 1;
        if (next == cur * 2) {
          q.unshift([next, time]);
        } else {
          q.push([next, time + 1]);
        }
      }
    }
  }
}

bfs(N);
