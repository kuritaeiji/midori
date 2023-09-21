N, T = [int(i) for i in input().split()]
books = []
for _ in range(N):
    page, days = [int(i) for i in input().split()]
    books.append({"page": page, "days": days})

memo = [-1 for _ in range(N)]


def dfs(n, sum_page=0, sum_days=0):
    if n == 0:
        return sum_page

    max_page = sum_page
    if sum_days + books[n - 1]["days"] <= T:
        max_page = dfs(
            n - 1, sum_page + books[n - 1]["page"], sum_days + books[n - 1]["days"]
        )

    max_page = max(dfs(n - 1, sum_page, sum_days), max_page)
    memo[n - 1] = max_page

    return max_page


print(dfs(N))
