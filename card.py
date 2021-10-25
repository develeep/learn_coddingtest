import sys
input = sys.stdin.readline
n, m = map(int, input().split())
result = 0
for i in range(n):
    x = list(map(int, input().split()))
    if result < min(x):
        result = min(x)
print(result)
