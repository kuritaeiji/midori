class UnionFind:
    def __init__(self, n):
        # n=全体の大きさ
        # 自分が根である場合は-1
        self.parents = [-1 for _ in range(n)]
        # 木のサイズ
        self.sizes = [1 for _ in range(n)]

    def root(self, x):
        if self.parents[x] == -1:
            return x

        my_root = self.root(self.parents[x])
        self.parents[x] = my_root
        return my_root

    def is_same(self, x, y):
        self.root(x) == self.root(y)

    def unite(self, x, y):
        root_x = self.root(x)
        root_y = self.root(y)
        # すでに同じグループの場合はreturn
        if root_x == root_y:
            return

        if self.sizes[root_x] < self.sizes[root_y]:
            self.parents[root_x] = root_y
            self.sizes[root_y] += self.sizes[root_x]
        else:
            self.parents[root_y] = root_x
            self.sizes[root_x] = self.sizes[root_y]


S = input()
T = input()

dp = [[-1 for _ in range(len(T))] for _ in range(len(S))]


def dfs(s_num, t_num, s, t, dp):
    if s_num == 0 or t_num == 0:
        if s_num == 0 and t_num == 0:
            return 0
        else:
            return 1

    if dp[s_num - 1][t_num - 1] != -1:
        return dp[s_num - 1][t_num - 1]

    if s[s_num - 1] == t[t_num - 1]:
        min_count = dfs(s_num - 1, t_num - 1, s, t, dp)
    else:
        min_count = dfs(s_num - 1, t_num - 1, s, t, dp) + 1

    min_count = min(min_count, dfs(s_num - 1, t_num, s, t, dp) + 1)
    min_count = min(min_count, dfs(s_num, t_num - 1, s, t, dp) + 1)

    dp[s_num - 1][t_num - 1] = min_count

    return min_count


print(dfs(len(S), len(T), S, T, dp))
