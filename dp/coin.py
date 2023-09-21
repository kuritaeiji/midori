import sys
import io
from collections import deque

sys.setrecursionlimit(10**7)

INPUT = """\
55 4
1 5 10 50
"""

sys.stdin = io.StringIO(INPUT)

# コイン問題
N, M = [int(i) for i in input().split()]
coins = [int(i) for i in input().split()]

dp = [-1 for _ in range(N + 1)]


def dfs(n, dp):
    if n == 0:
        return 0

    if dp[n] != -1:
        return dp[n]

    count = sys.maxsize
    for coin in coins:
        if n - coin >= 0:
            count = min(dfs(n - coin, dp) + 1, count)

    dp[n] = count
    return count


print(dfs(N, dp))
