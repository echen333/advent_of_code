
import string

f = open("day11.txt", "r")
lines = f.readlines()

grid = []
for line in lines:
    grid.append(list(line.strip()))

n = len(grid)
m = len(grid[0])
num = [[1e9 for i in range(m)] for j in range(n)]

ed = None
for i in range(n):
    for j in range(m):
        if grid[i][j] == "S":
            grid[i][j] = "a"
        elif grid[i][j] == "E":
            st = (i, j)
            grid[i][j] = "z"

def leg(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    return True

q = []
q.append(st)
num[st[0]][st[1]] = 0
while len(q) > 0:
    x, y = q.pop(0)
    for i, j in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        if leg(i, j) and string.ascii_lowercase.index(grid[i][j]) >= string.ascii_lowercase.index(grid[x][y]) - 1 and num[i][j] > num[x][y] + 1:
            num[i][j] = num[x][y] + 1
            q.append((i, j))

mn = 1e9
for i in range(n):
    for j in range(m):
        if grid[i][j] == "a":
            mn = min(mn, num[i][j])

print(mn)
