# AtCoder Typical Contest 001
# A - 深さ優先探索
# https://atcoder.jp/contests/atc001/tasks/dfs_a

import sys
sys.setrecursionlimit(1000000)


class GoalFound(Exception):
    pass

class Solver:
    def __init__(self, H, W, maze) -> None:
        self.H = H
        self.W = W
        self.maze = maze

    def find_point(self, obj):
        for h in range(self.H):
            for w in range(self.W):
                if self.maze[h][w] == obj:
                    return (h, w)
        raise ValueError('Not found:{}'.format(obj))

    def depth_first_search(self, h, w):
        if not (0 <= h < self.H):
            return False
        if not (0 <= w < self.W):
            return False
        if self.maze[h][w] == "g":
            raise GoalFound()
        if self.maze[h][w] == "#":
            return False
        if self.maze[h][w] in [".", "s"]:
            self.maze[h][w] = "#"
            return any([
                self.depth_first_search(h - 1, w),
                self.depth_first_search(h, w - 1),
                self.depth_first_search(h, w + 1),
                self.depth_first_search(h + 1, w)
            ])
        return False

    def solve(self) -> str:
        start = self.find_point('s')
        try:
            self.depth_first_search(*start)
            return 'No'
        except GoalFound:
            return 'Yes'


if __name__ == "__main__":
    H, W = list(map(int, input().split()))
    maze = []
    for _ in range(H):
        maze.append(list(input()))

    s = Solver(H, W, maze)
    print(s.solve())
