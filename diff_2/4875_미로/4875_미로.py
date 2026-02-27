#31

def dfs(x,y,mapp,visited,N):
    visited[x][y] = True

    if mapp[x][y] == 3:
            return 1
    
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    
    for next in range(4):
        nx = dx[next] + x
        ny = dy[next] + y
        
        if 0 <= nx < N and 0 <= ny < N and mapp[nx][ny] != 1 and not visited[nx][ny]:
            if dfs(nx,ny,mapp,visited,N) == 1:
                return 1
    return 0
                
    



T = int(input())

for i in range(T):
    N = int(input())
    mapp = [[]for _ in range(N)]
    visited = [[False for _ in range(N)] for _ in range(N)]
    x = 0
    y = 0
    for j in range(N):
        mapp[j] = list(map(int,input()))
        if 2 in mapp[j]:
            x = j
            y = mapp[j].index(2)
    print(f"#{i+1} {dfs(x,y,mapp,visited,N)}")

