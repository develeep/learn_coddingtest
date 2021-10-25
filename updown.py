import sys
input = sys.stdin.readline
n = int(input())
paths = input().split()

x, y = 1, 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
m = ['L', 'R', 'U', 'D']

for path in paths:
    for i in range(len(m)):
        if path == m[i]:
            nx = x+dx[i]
            ny = y+dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny
print(x, y)
