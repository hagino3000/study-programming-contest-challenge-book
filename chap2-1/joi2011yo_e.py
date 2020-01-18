# チーズ
# https://atcoder.jp/contests/joi2011yo/tasks/joi2011yo_e
from collections import deque

class GoalFound(Exception):
    def __init__(self, distance):
        self.distance = distance


class Solver:
    def __init__(self, H, W, N, maze) -> None:
        self.H = H
        self.W = W
        self.N = N
        self.maze = maze
        self.visited = set()
        self.queue = deque([])

    def find_start_pos(self):
        for h in range(self.H):
            line = self.maze[h]
            for w in range(self.W):
                if line[w] == 'S':
                    return (h, w)
        raise ValueError('Not found:S')

    def lookup(self, pos):
        y, x = pos
        return self.maze[y][x]

    def breadth_first_search(self, pos, distance, life, tile):
        if tile == str(life):
            if life == self.N:
                raise GoalFound(distance)
            else:
                life += 1
                self.queue.clear()
                self.visited = set()

        self.visited.add(pos)

        for dy, dx in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            y = pos[0] + dy
            x = pos[1] + dx

            if (0 <= y < self.H) and (0 <= x < self.W) and (y, x) not in self.visited:
                next_tile = self.lookup((y, x))
                if next_tile != 'X':
                    self.queue.append(((y, x), distance + 1, life, next_tile))
                    self.visited.add((y, x))

    def solve(self) -> int:
        self.queue.append((self.find_start_pos(), 0, 1, 'S'))
        try:
            while True:
                task = self.queue.popleft()
                self.breadth_first_search(*task)
        except GoalFound as e:
            return e.distance


if __name__ == "__main__":
    H, W, N = list(map(int, input().split()))
    maze = []
    for _ in range(H):
        maze.append(list(input()))

    s = Solver(H, W, N, maze)
    print(s.solve())
