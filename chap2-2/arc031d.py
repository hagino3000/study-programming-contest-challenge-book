# ARC031
# 埋め立て
# https://atcoder.jp/contests/arc031/tasks/arc031_2
LAND = "o"
SEA = "x"


class Solver:
    def __init__(self, field) -> None:
        self.S = 10
        self.field = field

    def count_land(self, h, w, visited, fill=False):
        if not (0 <= h < self.S):
            return 0
        if not (0 <= w < self.S):
            return 0
        if visited[h][w]:
            return 0
        if self.field[h][w] == LAND or fill:
            visited[h][w] = True
            return sum([
                1,
                self.count_land(h - 1, w, visited),
                self.count_land(h, w - 1, visited),
                self.count_land(h, w + 1, visited),
                self.count_land(h + 1, w, visited)
            ])
        if self.field[h][w] == SEA:
            return 0
        return 0

    def create_visit_map(self):
        return [
            [False for _ in range(10)]
            for _ in range(10)
        ]

    def count_lands(self):
        ret = 0
        for i in range(10):
            for j in range(10):
                ret += 1 if self.field[i][j] == LAND else 0
        return ret

    def solve(self) -> str:
        lands = self.count_lands()
        can_union = False
        for i in range(10):
            for j in range(10):
                if self.field[i][j] == SEA:
                    if self.count_land(i, j, self.create_visit_map(), True) == lands + 1:
                        can_union = True
                        break

        return 'YES' if can_union else 'NO'


if __name__ == "__main__":
    field = []
    for _ in range(10):
        field.append(list(input()))

    s = Solver(field)
    print(s.solve())
