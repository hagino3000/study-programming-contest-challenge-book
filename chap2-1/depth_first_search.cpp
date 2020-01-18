#include <cstdio>

using namespace std;

int a[] = {-3, -1, 0, 12, 30, 99, 100, 1024};
int n = 8;
//int k = 1150;
int k = 115199999;

bool dfs(int i, int sum) {
    if (i == n) return sum == k;

    if (dfs(i + 1, sum)) return true;

    if (dfs(i + 1, sum + a[i])) return true;

    return false;
}

int main() {
    if (dfs(0, 0)) {
        printf("Solved\n");
    } else {
        printf("Cannot solve\n");
    }
    return 0;
}
