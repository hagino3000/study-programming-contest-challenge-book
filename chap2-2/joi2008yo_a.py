# 問題: 第７回日本情報オリンピック 予選（オンライン）
# おつり
# https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_a
class Solver():

    def __init__(self, price):
        self.price = price

    def solve(self):
        ret = 0
        remain = 1000 - self.price
        for c in [500, 100, 50, 10, 5, 1]:
            unit = remain // c
            ret += unit
            remain = remain - c * unit
            if remain == 0:
                break
        return ret


if __name__ == "__main__":
    n = int(input())
    s = Solver(n)
    print(s.solve())
