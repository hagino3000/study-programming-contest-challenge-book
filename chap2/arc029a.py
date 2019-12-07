from copy import deepcopy
from typing import List


n = int(input())
t = []
for _ in range(n):
    t.append(int(input()))


def depth_first_search(niku_index: int, yaki_index: int, cumulative_times: List[int]) -> int:
    cumulative_times[yaki_index] += t[niku_index]
    if niku_index == n - 1:
        return max(cumulative_times)

    return min(
        depth_first_search(niku_index + 1, 0, deepcopy(cumulative_times)),
        depth_first_search(niku_index + 1, 1, deepcopy(cumulative_times))
    )


def solve() -> int:
    return min(
        depth_first_search(0, 0, [0, 0]),
        depth_first_search(0, 1, [0, 0])
    )


if __name__ == "__main__":
    print(solve())
