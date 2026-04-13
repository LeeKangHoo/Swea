# 9
# 가로가 x 세로가 y
# 출발지부터 도착지까지 길이 있는지 판단하는 프로그램

from collections import deque

def bfs(start,mapp):
    visited = [[False] * 16 for _ in range(16)]
    visited[start[0]][start[1]] = True
    q = deque()
    q.append(start)

    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    while q:
        cx, cy = q.popleft()
        if mapp[cx][cy] == '3':
            return 1
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < 16 and 0 <= ny < 16 and mapp[nx][ny] != '1' and not visited[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny] = True
    return 0
    

for _ in range(10):
    tc = int(input())
    mapp = [input() for _ in range(16)]
    start = (0,0)
    f = False
    for i in range(16):
        if f:
            break
        for j in range(16):
            if mapp[i][j] == '2':
                start = (i,j)
                f = True
                break

    print(f'#{tc} {bfs(start,mapp)}')
