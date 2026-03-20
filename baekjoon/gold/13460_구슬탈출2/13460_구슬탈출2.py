#X
from collections import deque

def move(x, y, dx, dy, mapp):
    cnt = 0
    while mapp[x+dx][y+dy] != '#' and mapp[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt

def bfs(rx, ry, bx, by, mapp):
    q = deque()
    q.append((rx, ry, bx, by, 0))
    visited = set()
    visited.add((rx, ry, bx, by))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        crx, cry, cbx, cby, depth = q.popleft()

        if depth >= 10:
            continue

        for i in range(4):
            nrx, nry, r_cnt = move(crx, cry, dx[i], dy[i], mapp)
            nbx, nby, b_cnt = move(cbx, cby, dx[i], dy[i], mapp)

            if mapp[nbx][nby] == 'O':
                continue
            if mapp[nrx][nry] == 'O':
                return depth + 1

            if nrx == nbx and nry == nby:
                if r_cnt > b_cnt:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]

            if (nrx, nry, nbx, nby) not in visited:
                visited.add((nrx, nry, nbx, nby))
                q.append((nrx, nry, nbx, nby, depth + 1))
                
    return -1

N, M = map(int, input().split())
mapp = []
rx, ry, bx, by = 0, 0, 0, 0

for i in range(N):
    row = list(input())
    mapp.append(row)
    for j in range(M):
        if row[j] == 'R':
            rx, ry = i, j
            mapp[i][j] = '.'
        elif row[j] == 'B':
            bx, by = i, j
            mapp[i][j] = '.'

print(bfs(rx, ry, bx, by, mapp))