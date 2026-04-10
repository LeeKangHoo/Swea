# X
# N * N 에서 상하좌우로 이동하는데, 이동하려는 방에 적힌 숫자가 현재 방보다 정확히 1 커야한다.
# 어디서 시작해야 가장 많은 개수의 방을 이동할 수 있는가? 그리고 몇 칸을 이동하는가?
# 보기에는 그냥 dfs 백트래킹으로 모든 방 탐색하는건데 왜 D4문제일까 
# 백트래킹도 필요없네 무조건 하나의 경로네
# 제출하니까 27/24. 엣지 케이스가 뭘까

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def dfs(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and room[nx][ny] - room[x][y] == 1:
            visited[nx][ny] = visited[x][y] + 1
            return dfs(nx,ny) + 1
            
    return 1

    


T = int(input())

for tc in range(T):
    N = int(input())
    room = [list(map(int,input().split())) for _ in range(N)]
    
    max_val = 1
    r = 0
    for i in range(N):
        for j in range(N):
            visited = [[0] * N for _ in range(N)]
            d = dfs(i,j)
            val = room[i][j]
            if max_val < d:
                r = val
                max_val = d
            elif max_val == d:
                if r == 0 or r > val:
                    r = val
                

    print(f'#{tc+1} {r} {max_val}')


