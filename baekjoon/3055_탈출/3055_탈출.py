#64
from collections import deque
def bfs(mapp):
    q = deque()
    D, S = (0,0), (0,0)
    water_t = set()
    for i in range(R):
        if 'D' in mapp[i]:
            D = (i,mapp[i].index('D'))
        if 'S' in mapp[i]:
            S = (i,mapp[i].index('S'))
        if '*' in mapp[i]:
            water_t.add((i,mapp[i].index('*')))
    q.append((S[0],S[1],water_t))
    visited = [[0] * C for _ in range(R)]


    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    while q:
        cx, cy, water = q.popleft()
        if cx == D[0] and cy == D[1]:
            return visited[cx][cy]

        # water pollution
        new_water = set(water)
        for i in water:
            for j in range(4):
                wx = i[0] + dx[j]
                wy = i[1] + dy[j]
                if 0 <= wx < R and 0 <= wy < C and mapp[wx][wy] == '.':
                    new_water.add((wx,wy))
        
        # main bfs
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < R and 0 <= ny < C and (nx,ny) not in new_water and mapp[nx][ny] != 'X' and visited[nx][ny] == 0:
                visited[nx][ny] = visited[cx][cy] + 1
                q.append((nx,ny,new_water))
        

    return 'KAKTUS'



R, C = map(int,input().split())
mapp = []


for i in range(R):
    mapp.append(list(input()))

print(bfs(mapp))