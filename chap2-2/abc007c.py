# ABC007 C 幅優先探索
# https://atcoder.jp/contests/abc007/tasks/abc007_3

from collections import deque

class GoalFound(Exception):
    def __init__(self, distance):
        self.distance = distance

class Solver:
    def __init__(self, R, C, start, goal, maze) -> None:
        self.R = R
        self.C = C
        self.start = start
        self.goal = goal
        self.maze = maze
        self.visited = set()
        self.queue = deque([])

    def lookup(self, y, x):
        return self.maze[y-1][x-1]  # to zero origin

    def breadth_first_search(self, y, x, distance):
        if (y, x) == self.goal:
            raise GoalFound(distance)
        if (y, x) in self.visited:
            return
        if not (1 <= y <= self.R):
            return
        if not (1 <= x <= self.C):
            return
        if self.lookup(y, x) == "#":
            return
        if self.lookup(y, x) == ".":
            self.visited.add((y, x))
            self.queue.append((y - 1, x, distance + 1))
            self.queue.append((y, x - 1, distance + 1))
            self.queue.append((y, x + 1, distance + 1))
            self.queue.append((y + 1, x, distance + 1))

    def solve(self) -> int:
        self.queue.append((self.start[0], self.start[1], 0))
        try:
            while len(self.queue) > 0:
                task = self.queue.popleft()
                self.breadth_first_search(*task)
        except GoalFound as e:
            return e.distance


if __name__ == "__main__":
    R, C = list(map(int, input().split()))
    start = tuple(map(int, input().split()))
    goal = tuple(map(int, input().split()))
    maze = []
    for _ in range(R):
        maze.append(list(input()))

    s = Solver(R, C, start, goal, maze)
    print(s.solve())
