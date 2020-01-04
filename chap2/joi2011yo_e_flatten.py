# チーズ
# https://atcoder.jp/contests/joi2011yo/tasks/joi2011yo_e
from collections import deque

H, W, N = list(map(int, input().split()))
maze = []
for _ in range(H):
    maze.append(list(input()))


visited = set()
queue = deque([])


def find_start_pos():
    for h in range(H):
        line = maze[h]
        for w in range(W):
            if line[w] == 'S':
                return (h, w)
    raise ValueError('Not found:S')


candidates = [(-1, 0), (0, -1), (0, 1), (1, 0)]
queue.append((find_start_pos(), 0, 1, 'S'))
while True:
    pos, distance, life, tile = queue.popleft()
    if tile == str(life):
        if life == N:
            print(distance)
            break
        else:
            life += 1
            queue.clear()
            visited = set()

    visited.add(pos)

    for dy, dx in candidates:
        y = pos[0] + dy
        x = pos[1] + dx

        if (0 <= y < H) and (0 <= x < W) and (y, x) not in visited:
            next_tile = maze[y][x]
            if next_tile != 'X':
                queue.append(((y, x), distance + 1, life, next_tile))
                visited.add((y, x))
