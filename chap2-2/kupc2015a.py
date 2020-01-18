# 問題; 京都大学プログラミングコンテスト2015 a
# A - 東京都
# https://atcoder.jp/contests/kupc2015/tasks/kupc2015_a?lang=ja
class Solver:
    def __init__(self, n, cases):
        self.n = n
        self.cases = cases

    def solve(self):
        for test_case in self.cases:
            start, end, tapes = 0, 1, 0
            while True:
                target = test_case[start:end]
                if 'tokyo' in target or 'kyoto' in target:
                    tapes += 1
                    start = end
                if end == len(test_case):
                    break
                end += 1
            print(tapes)


if __name__ == "__main__":
    n = int(input())
    cases = []
    for _ in range(n):
        cases.append(input())

    s = Solver(n, cases)
    s.solve()
