# AtCoder Beginner Contest 002
# D - 派閥
# https://abc002.contest.atcoder.jp/tasks/abc002_4
from itertools import combinations


def power_set(size: int):
    items = [i+1 for i in range(size)]
    for i in range(size+1):
        yield from combinations(items, i)


class Solver:
    def __init__(self, N, M, edges) -> None:
        self.N = N
        self.edge_set = frozenset(edges)

    def check_constraint_satisfaction(self, habatsu: set) -> bool:
        if len(habatsu) <= 1:
            return True

        for i in habatsu:
            for k in habatsu:
                if i != k and i < k:
                    if not (i, k) in self.edge_set:
                        return False
        return True

    def solve(self) -> int:
        # 派閥の全組合せ列挙
        possible_habatsu_set = power_set(self.N)

        member_count = []
        for habatsu in possible_habatsu_set:
            if self.check_constraint_satisfaction(habatsu):
                member_count.append(len(habatsu))

        return max(member_count)


if __name__ == "__main__":
    N, M = list(map(int, input().split()))
    edges = []
    for _ in range(M):
        edges.append(tuple(map(int, input().split())))

    s = Solver(N, M, edges)
    print(s.solve())
