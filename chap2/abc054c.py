# https://atcoder.jp/contests/abc054/tasks/abc054_c
# C - One-stroke Path

class Solver:
    def __init__(self, N, M, edges) -> None:
        self.N = N
        self.M = M
        self.edges = edges

    def find_next_node(self, current, visited):
        candidates = []
        for edge in self.edges:
            if edge[0] == current:
                candidates.append(edge[1])
            if edge[1] == current:
                candidates.append(edge[0])
        ret = []
        for node in candidates:
            bit = 2**(node - 1)
            if visited & bit == 0:
                # AND演算でゼロの場合は未訪問ノード
                ret.append(node)
        return ret

    def dfs(self, node, visited):
        """
        visitedのn番目のビットでノードnを訪ずれたか管理する
        """
        visited += 2**(node - 1)
        if visited == 2**self.N - 1:
            # フルビット立っていたら全ノード訪問済み
            return 1
        movable_nodes = self.find_next_node(node, visited)
        return sum([self.dfs(next_node, visited) for next_node in movable_nodes])


    def solve(self) -> int:
        return self.dfs(1, 0)


if __name__ == "__main__":
    N, M = list(map(int, input().split()))
    edges = []
    for _ in range(M):
        edges.append(list(map(int, input().split())))

    s = Solver(N, M, edges)
    print(s.solve())
