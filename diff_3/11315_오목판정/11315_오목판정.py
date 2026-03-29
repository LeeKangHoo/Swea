#42
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

cx = [0,0]
cy = [-1,1]
rx = [-1,1]
ry = [0,0]
d1x = [-1,1]
d1y = [-1,1]
d2x = [-1,1]
d2y = [1,-1]

D = ['c','r','d1','d2']

def dfs(x,y,d):
    cnt = 0
    if d == 0:
        for i in range(2):
            nx = cx[i] + x
            ny = cy[i] + y
            if 0 <= nx < N and 0 <= ny < N and pan[nx][ny] == 'o' and not visited[nx][ny][d]:
                visited[nx][ny][d] = True
                cnt += dfs(nx,ny,d) + 1
    elif d == 1:
        for i in range(2):
            nx = rx[i] + x
            ny = ry[i] + y
            if 0 <= nx < N and 0 <= ny < N and pan[nx][ny] == 'o' and not visited[nx][ny][d]:
                visited[nx][ny][d] = True
                cnt += dfs(nx,ny,d) + 1
    elif d == 2:
        for i in range(2):
            nx = d1x[i] + x
            ny = d1y[i] + y
            if 0 <= nx < N and 0 <= ny < N and pan[nx][ny] == 'o' and not visited[nx][ny][d]:
                visited[nx][ny][d] = True
                cnt += dfs(nx,ny,d) + 1
    elif d == 3:
        for i in range(2):
            nx = d2x[i] + x
            ny = d2y[i] + y
            if 0 <= nx < N and 0 <= ny < N and pan[nx][ny] == 'o' and not visited[nx][ny][d]:
                visited[nx][ny][d] = True
                cnt += dfs(nx,ny,d) + 1

    return cnt

def solve(x,y,pan,visited):
    flag = False

    for next in range(4):
        if not visited[x][y][next]:
            if dfs(x,y,next) >= 5:
                flag = True
                break
    if flag:
        return 'YES'
    return 'NO'


    
    
    


T = int(input())

for tc in range(T):
    N = int(input())

    pan = [input() for _ in range(N)]
    visited = [[[False] * 4 for _ in range(N)] for _ in range(N)]
    r = ''
    f = False
    for i in range(N):
        if not f:
            for j in range(N):
                if pan[i][j] == 'o':
                    if solve(i,j,pan,visited) == 'YES':
                        f = True
                        print(f"#{tc+1} YES")
                        break
    
    if not f:
        print(f"#{tc+1} NO")
                        
                