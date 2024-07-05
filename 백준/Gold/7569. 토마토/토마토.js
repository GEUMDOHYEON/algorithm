const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "JS/example.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [M, N, H] = input.shift().split(" ").map(Number);
const queue = [];
const boxes = Array.from(Array(H), () =>
  Array.from(Array(N), () => Array.from(Array(M).fill(0)))
);
const dx = [-1, 1, 0, 0, 0, 0];
const dy = [0, 0, -1, 1, 0, 0];
const dz = [0, 0, 0, 0, -1, 1];

// 3차원 배열에 입력값 삽입
for (let i = 0; i < H; i++) {
  for (let j = 0; j < N; j++) {
    boxes[i][j] = input.shift().split(" ").map(Number);
  }
}

let unripeTomato = 0;
for (let i = 0; i < H; i++) {
  for (let j = 0; j < N; j++) {
    for (let k = 0; k < M; k++) {
      // 익지 않은 토마토이면 카운트 증가
      if (boxes[i][j][k] == 0) unripeTomato++;
      // 익은 토마토이면 큐에 담기 (현재 위치 및 걸린 일수 초기값 0)
      if (boxes[i][j][k] == 1) queue.push([i, j, k, 0]);
    }
  }
}

let idx = 0;
let answer = 0;

while (queue.length > idx) {
  const [z, x, y, days] = queue[idx++];

  for (let i = 0; i < 6; i++) {
    const nx = x + dx[i];
    const ny = y + dy[i];
    const nz = z + dz[i];

    if (
      0 <= nx &&
      nx < N &&
      0 <= ny &&
      ny < M &&
      0 <= nz &&
      nz < H &&
      !boxes[nz][nx][ny]
    ) {
      boxes[nz][nx][ny] = 1;
      queue.push([nz, nx, ny, days + 1]);
      unripeTomato--;
    }
  }
  answer = days;
}

console.log(unripeTomato ? -1 : answer);
