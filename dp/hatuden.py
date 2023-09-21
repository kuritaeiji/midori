import sys
import io
from collections import deque

sys.setrecursionlimit(10**7)

INPUT = """\
4
3 7 4 8
0 5 9 7
0 0 8 5
0 0 0 6 
"""

sys.stdin = io.StringIO(INPUT)

# 発電計画問題
# 区間に区切る問題

T = int(input())
benefits = []
for _ in range(T):
    benefits.append([int(i) for i in input().split()])

dp = [-1 for _ in range(T + 1)]


# t秒まで発電可能な最大利得を返却する
def dfs(t, benefits, dp):
    if t <= 0:
        return 0

    if dp[t] != -1:
        return dp[t]

    # i秒からj秒まで発電をオンにしていた場合の最大利得
    # t=４の場合以下のパターンのときに発電所を動かした場合の最大利得を求める
    # 0-1,0-2,0-3,0-4
    # 1-2,1-3,1-4
    # 2-3,2-4
    # 3-4
    # 例えば3-4で発電所を動かす場合、2秒まで発電所を動かした場合の最大利得+発電所を3秒-4秒動かした場合の利得を求めれば良い
    max_benefit = 0
    for i in range(t + 1):
        for j in range(i + 1, t + 1):
            max_benefit = max(
                dfs(i - 1, benefits, dp) + benefits[i][j - 1], max_benefit
            )

    dp[t] = max_benefit

    return max_benefit


print(dfs(T, benefits, dp))
