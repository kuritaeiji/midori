import sys
import io
import copy
from collections import deque

sys.setrecursionlimit(10**7)

INPUT = """\
10 5
3 5 4 9 11 8 10 1 7 8
"""

sys.stdin = io.StringIO(INPUT)

N, K = [int(i) for i in input().split()]
oranges = [int(i) for i in input().split()]

dp = [-1 for _ in range(len(oranges) + 1)]
dp[0] = 0


def cost(start, end, oranges, k):
    max_num = 0
    min_num = sys.maxsize
    for i in range(start - 1, end):
        max_num = max(oranges[i], max_num)
        min_num = min(oranges[i], min_num)
    return k + (max_num - min_num) * (end - start + 1)


# n個目のオレンジまで箱に詰める時の最小コスト（1からかぞえる）
def dfs(n, oranges, k, dp):
    if n == 0:
        return 0

    if dp[n] != -1:
        return dp[n]

    min_num = sys.maxsize
    # i個目までの最小コスト+(i+1個目からn個目までを同じ箱に入れた場合のコストを計算していく)
    for i in range(n):
        min_num = min(dfs(i, oranges, k, dp) + cost(i + 1, n, oranges, k), min_num)

    dp[n] = min_num
    return min_num


a = dfs(N, oranges, K, dp)
print(a)
