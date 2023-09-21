import sys
import io
import math
import itertools


INPUT = """\
15 158260522
877914575 2436426
24979445 61648772
623690081 33933447
476190629 62703497
211047202 71407775
628894325 31963982
822804784 50968417
430302156 82631932
161735902 80895728
923078537 7723857
189330739 10286918
802329211 4539679
303238506 17063340
492686568 73361868
125660016 50287940
"""

sys.stdin = io.StringIO(INPUT)

N, K = [int(i) for i in input().split()]
medicines = []
for _ in range(N):
    medicines.append([int(i) for i in input().split()])

sum = 0
for medicine in medicines:
    sum += medicine[1]

medicines.sort()


def calc_count(n):
    count = sum
    for medicine in medicines:
        if medicine[0] < n:
            count -= medicine[1]
        else:
            return count
    return count


# leftは条件を満たさない日付
left = 1
# rightは条件を満たす日付
right = 10**9 + 1

# leftは条件を満たさない日付でなければならないため初期値1日目がすでに条件を満たしていた場合exitする
if sum <= K:
    print(1)
    exit()

while right - left > 1:
    middle = (right - left) // 2 + left
    if calc_count(middle) <= K:
        right = middle
    else:
        left = middle

print(right)
