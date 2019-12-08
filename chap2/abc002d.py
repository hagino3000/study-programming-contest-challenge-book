# AtCoder Beginner Contest 002
# D - 派閥
# https://abc002.contest.atcoder.jp/tasks/abc002_4

class Solver:
    def __init__(self, N, M, edges) -> None:
        self.N = N
        self.edge_set = frozenset(edges)

    def power_set(self, m: int, tmp: set, accumulator: set) -> set:
        if m == self.N:
            accumulator.add(tmp)
            return
        self.power_set(m+1, tmp, accumulator)
        self.power_set(m+1, tmp.union([m+1]), accumulator)
        return accumulator

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
        possible_habatsu_set = self.power_set(0, frozenset(), set())

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
