import sys
import io
from collections import deque

sys.setrecursionlimit(10**7)

INPUT = """\
5 8
0 1 2
1 2 2
2 4 2
2 3 5
3 0 2
3 4 2
4 3 2
4 0 1
"""

sys.stdin = io.StringIO(INPUT)

# bitDPは集合から1個づつ頂点を減らしていく感じ

V, E = [int(i) for i in input().split()]
graph = [[-1 for _ in range(V)] for _ in range(V)]
for _ in range(E):
    s, t, d = [int(i) for i in input().split()]
    graph[s][t] = d

dp = [[-1 for _ in range(V)] for _ in range((1 << V) + 1)]


def dfs(s, end, dp):
    if s == 0 and end == 0:
        return 0
    if s == 0:
        return sys.maxsize

    if dp[s][end] != -1:
        return dp[s][end]

    min_cost = sys.maxsize
    for v in range(V):
        if not s >> v & 1:
            continue

        if graph[v][end] == -1:
            continue

        min_cost = min(min_cost, dfs(s - (1 << v), v, dp) + graph[v][end])

    dp[s][end] = min_cost

    return min_cost


S = (1 << V) - 1
min_cost = dfs(S, 0, dp)
if min_cost == sys.maxsize:
    print(-1)
else:
    print(min_cost)
