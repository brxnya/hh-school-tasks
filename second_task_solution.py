from collections import deque

n, m = map(int, input().split())
y1, x1 = map(int, input().split())
y2, x2 = map(int, input().split())
fields = []
for _ in range(n):
    fields.append(input().replace(' ', ''))

delta = [(0, -1), (0, 1), (1, 0), (-1, 0)]
d = [[-1] * m for _ in range(n)]
queue = deque()
d[x1][y1] = 0
res = 0

queue.append((x1, y1))
while queue:
    sx, sy = queue.popleft()
    if sx == x2 and sy == y2:
        res = d[x2][y2]
        break
    for dx, dy in delta:
        nx, ny = sx + dx, sy + dy
        if 0 <= nx < n and 0 <= ny < m and d[nx][ny] == -1 and fields[nx][ny] == '0':
            d[nx][ny] = d[sx][sy] + 1
            queue.append((nx, ny))
print(res)
