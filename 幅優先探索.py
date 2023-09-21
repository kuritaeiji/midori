import sys
import io
from collections import deque

sys.setrecursionlimit(10**7)

INPUT = """\
9 13
0 1
0 4
0 2
1 4
1 3
1 8
2 5
3 8
4 8
5 8
5 6
3 7
6 7
"""

sys.stdin = io.StringIO(INPUT)

N, E = [int(i) for i in input().split()]
graph = [[] for _ in range(N)]
for _ in range(E):
    a, b = [int(i) for i in input().split()]
    graph[a].append(b)
    graph[b].append(a)

dist = [-1 for _ in range(N)]
dist[0] = 0
queue = deque([])
queue.append(0)

while len(queue) > 0:
    vertex = queue.popleft()
    for next in graph[vertex]:
        if dist[next] != -1:
            continue
        dist[next] = dist[vertex] + 1
        queue.append(next)

for i in range(N - 1):
    print(dist[i + 1])
