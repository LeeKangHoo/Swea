#61
# dfs로 푸는 문제 같아서 시도
# for문을 돌려서 모든 방향을 해보는게 좋을 것 같다.

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def solve(x,y,d,mapp,visited):
    global cnt

    flag = False

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if mapp[nx][ny] == 0 and not visited[nx][ny]:
                flag = True
    
    if flag:
        for i in range(4):
            c = (d-i+3)%4
            nx = x + dx[c]
            ny = y + dy[c]
            if 0 <= nx < N and 0 <= ny < M and mapp[nx][ny] == 0:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    cnt += 1
                    solve(nx,ny,c,mapp,visited)
                    break

    else:
        td = (d+2)%4
        nx = x + dx[td]
        ny = y + dy[td]
        if 0 <= nx < N and 0 <= ny < M and mapp[nx][ny] == 0:
            solve(nx,ny,d,mapp,visited)
        else:
            return
    return 


N, M = map(int,input().split())

x,y,d = map(int,input().split())

mapp = [list(map(int,input().split())) for _ in range(N)]
a = 0
for i in range(N):
    a +=mapp[i].count(0)
visited = [[False]*M for _ in range(N)]
cnt = 0
visited[x][y] = True
cnt += 1
solve(x,y,d,mapp,visited)
print(cnt)