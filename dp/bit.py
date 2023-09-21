import sys
import io
from collections import deque

sys.setrecursionlimit(10**7)

INPUT = """\
4
0 8 7 3
8 0 9 1
7 9 0 4
3 1 4 0
"""

sys.stdin = io.StringIO(INPUT)

# bitDPは集合から1個づつ頂点を減らしていく感じ

N = int(input())
graph = []
for _ in range(N):
    graph.append([int(i) for i in input().split()])

dp = [[-1 for _ in range(N)] for _ in range(1 << N - 1)]


# 集合sには既にgoalの頂点は存在しないことを前提とする
# 集合sからgoalへの最短経路を求める
def dfs(s, goal):
    # 集合sから頂点がなくなったら終了
    if s == 0:
        return 0

    min_count = sys.maxsize

    # goalの手前の頂点としてuを全探索する
    for u in range(N):
        # 集合{s-goal}にuが存在しない場合はcontinue
        if not s >> u & 1:
            continue

        min_count = min(dfs(s - (1 << u), u) + graph[u][goal], min_count)

    return min_count


s = (1 << N) - 1
for i in range(N):
    print(dfs(s - (1 << i), i))

import sys
import io
from collections import deque

sys.setrecursionlimit(10**7)

INPUT = """\
2
OI
"""

sys.stdin = io.StringIO(INPUT)

N = int(input())
admin_chars = list(input())
admins = []
for admin in admin_chars:
    if admin == "J":
        admins.append(0)
    elif admin == "O":
        admins.append(1)
    else:
        admins.append(2)


def dfs(s, n):
    if n == 1 and s >> 0 & 1:
        return 1
    if n == 0:
        return 0

    patterns = 0
    # n-1日目の参加者を決める
    for i in range((1 << 3) - 1):
        # n-1日目の責任者がいない
        if not i >> admins[n - 2] & 1:
            continue

        # n-1日目の参加者の中で一人以上n日目の参加者がいる
        is_present = False
        for j in range(3):
            if s >> j & 1 and i >> j & 1:
                is_present = True
        if not is_present:
            continue

        patterns += dfs(i, n - 1)

    return patterns


patterns = 0
for i in range((1 << 3) - 1):
    if not i >> admins[N - 1] & 1:
        continue
    patterns += dfs(i, N)

print(patterns)
