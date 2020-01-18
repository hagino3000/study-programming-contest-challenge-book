# 第９回日本情報オリンピック 予選（オンライン）
# https://atcoder.jp/contests/joi2010yo/tasks/joi2010yo_d
from itertools import combinations, permutations


class Solver:
    def __init__(self, n, k, nums) -> None:
        self.n = n
        self.k = k
        self.nums = nums

    def solve(self) -> int:
        results = set()
        # 組合せ列挙
        for c in combinations(self.nums, k):
            # 順列作成
            for p in permutations(c):
                results.add(int(''.join(map(str, p))))
        return len(results)


if __name__ == "__main__":
    n = int(input())
    k = int(input())
    nums = []
    for _ in range(n):
        nums.append(int(input()))
    s = Solver(n, k, nums)
    print(s.solve())

