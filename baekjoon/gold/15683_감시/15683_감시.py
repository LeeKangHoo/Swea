#1시간 30분 초과
# 일단 CCTV 5개를 구현하고, cctv가 보는 경로를 따라 한칸한칸 확인할 함수 필요
# CCTV는 8개까지 존재 가능하고 같은 종류(번호)의 CCTV중복 가능
# 0은 빈칸, 6은 벽, 1~5는 CCTV
# 사각지대의 최소 크기를 구해야 하니까 다 돌아봐야함
# CCTV의 종류를 list에 따로 모아 두기
# CCTV가 90도씩 회전 가능하니까 for문을 range(4)로 해서 각 CCTV마다 방향을 돌리면 될듯. 그리고 idx를 써서 전에 확인한것도 안겹치게
# #을 칠 하고 나중에 지울까? 아니면 안칠하고 확인하는 방법을 사용해볼까? visited가 False인 곳을 count 하면 될 것 같다.
# direction(d)은 문제에 있는 기본 모양을 0번으로 지정 그리고 시계방향으로 회전
dx = [0,1,0,-1]
dy = [1,0,-1,0]
k = [4,2,4,4,1]
def look(x,y,kind,d,do):
    if kind == 1:
        nx, ny = x,y
        while 0 <= nx < N and 0 <= ny < M:
            nx = nx + dx[d]
            ny = ny + dy[d]
            
            if 0 <= nx < N and 0 <= ny < M:
                if room[nx][ny] == 6:
                    break
                visited[nx][ny] += do
    elif kind == 2:

        for i in range(2):
            nx, ny = x,y
            while 0 <= nx < N and 0 <= ny < M:
                nx = nx + dx[(d+2*i)%4]
                ny = ny + dy[(d+2*i)%4]
                
                if 0 <= nx < N and 0 <= ny < M:
                    if room[nx][ny] == 6:
                        break
                    visited[nx][ny] += do
    elif kind == 3:
        for i in range(2):
            # i 는 화살표의 갯수 구나
            nx, ny = x,y
            while 0 <= nx < N and 0 <= ny < M:
                nx = nx + dx[(d+3*i)%4]
                ny = ny + dy[(d+3*i)%4]
                
                if 0 <= nx < N and 0 <= ny < M:
                    if room[nx][ny] == 6:
                        break
                    visited[nx][ny] += do
    elif kind == 4:
        for i in range(3):
            nx, ny = x,y
            while 0 <= nx < N and 0 <= ny < M:
                nx = nx + dx[(d+i+2)%4]
                ny = ny + dy[(d+i+2)%4]
                
                if 0 <= nx < N and 0 <= ny < M:
                    if room[nx][ny] == 6:
                        break
                    visited[nx][ny] += do
    elif kind == 5:
        for i in range(4):
            nx, ny = x,y
            while 0 <= nx < N and 0 <= ny < M:
                nx = nx + dx[i]
                ny = ny + dy[i]
                
                if 0 <= nx < N and 0 <= ny < M:
                    if room[nx][ny] == 6:
                        break
                    visited[nx][ny] += do
    return
def solve(idx):
    global min_val
    if idx == len(cctv):
        r = 0
        for i in range(N):
            r += visited[i].count(-1)
        min_val = min(min_val,r)
        return


    cx,cy,kind = cctv[idx]
    for j in range(k[kind-1]):
        look(cx,cy,kind,j,1)
        solve(idx+1)
        look(cx,cy,kind,j,-1)

    


N, M = map(int,input().split())

room = [list(map(int,input().split())) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]
cctv = []
# cctv 위치 미리 받아놓기
for i in range(N):
    for j in range(M):
        if room[i][j] in [1,2,3,4,5]:
            visited[i][j] = 1
            cctv.append((i,j,room[i][j]))
        elif room[i][j] == 6:
            visited[i][j] = 1
min_val = 10**8
solve(0)
print(min_val)