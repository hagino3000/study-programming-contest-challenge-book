# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_B&lang=jp#
# AOJ0-1 ナップザック問題

from collections import namedtuple
from functools import lru_cache

Item = namedtuple('Item', ('v', 'w'))


class Solver():
    def __init__(self, N, W, items):
        self.N = N
        self.W = W
        self.items = items

    @lru_cache(maxsize=None)
    def dfs(self, w, index):
        item = items[index]
        if index == self.N - 1:
            if w + item.w <= self.W:
                return item.v
            else:
                return 0

        if w + item.w <= self.W:
            return max([
                # skip this item
                self.dfs(w, index + 1),
                # Store this item
                item.v + self.dfs(w+item.w, index + 1)
            ])
        else:
            # Skip this item
            return self.dfs(w, index + 1)

    def solve(self):
        # 重さゼロの状態でゼロ番目の品物から評価
        return self.dfs(0, 0)


if __name__ == "__main__":
    N, W = list(map(int, input().split()))
    items = []
    for _ in range(N):
        v, w = list(map(int, input().split()))
        items.append(Item(v=v, w=w))

    s = Solver(N, W, items)
    print(s.solve())
