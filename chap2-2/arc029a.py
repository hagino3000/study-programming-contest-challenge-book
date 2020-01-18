# 問題:  AtCoder Regular Contest 029
# 高橋君とお肉
# https://arc029.contest.atcoder.jp/tasks/arc029_1
from copy import deepcopy
from typing import List


class Solver():
    def __init__(self, n, t):
        self.n = n
        self.t = t

    def depth_first_search(
            self,
            niku_index: int,
            yaki_index: int,
            cumulative_times: List[int]) -> int:

        # 肉焼き器毎の焼き時間に加算
        cumulative_times[yaki_index] += self.t[niku_index]
        if niku_index == self.n - 1:
            return max(cumulative_times)

        return min(
            self.depth_first_search(niku_index + 1, 0, deepcopy(cumulative_times)),
            self.depth_first_search(niku_index + 1, 1, deepcopy(cumulative_times))
        )

    def solve(self) -> int:
        # 深さ優先探索ですべてのパターンを走査
        return min(
            self.depth_first_search(0, 0, [0, 0]),
            self.depth_first_search(0, 1, [0, 0])
        )


if __name__ == "__main__":
    n = int(input())
    t = []
    for _ in range(n):
        t.append(int(input()))

    s = Solver(n, t)
    print(s.solve())
