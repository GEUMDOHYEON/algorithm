const filePath = process.platform === "linux" ? "/dev/stdin" : "JS/example.txt";

const input = require("fs")
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map((v) => v.split(" ").map(Number));

const [N, M] = input.shift();
const dx = [1, -1, 0, 0];
const dy = [0, 0, -1, 1];
const result = [];

function bfs(a, b) {
  const q = [];
  q.push([a, b]);
  let count = 1;
  input[a][b] = 0;

  while (q.length > 0) {
    const [x, y] = q.shift();

    for (let i = 0; i < 4; i++) {
      let nx = x + dx[i];
      let ny = y + dy[i];

      if (0 <= nx && nx < N && 0 <= ny && ny < M && input[nx][ny] === 1) {
        input[nx][ny] = 0;
        count++;
        q.push([nx, ny]);
      }
    }
  }
  return count;
}

for (let i = 0; i < N; i++) {
  for (let j = 0; j < M; j++) {
    if (input[i][j] === 1) {
      result.push(bfs(i, j));
    }
  }
}
console.log(result.length);
if (result.length === 0) {
  console.log(0);
} else {
  console.log(Math.max(...result));
}
