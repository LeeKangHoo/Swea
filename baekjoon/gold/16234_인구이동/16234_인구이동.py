#X
# 한 시퀀스 단위로 하는데, 인구 차이가 L <= 인구차이 <= R 인곳부터 시작해서 인구수를 공유할 "연합" 국가를 넓힌다.(어디까지 가능한지)
# 인구수를 공유하고 난 후로는 다시 탐색해서 L <= 인구차이 <= R 의 경우에 부합하는 경우를 찾는다.
# 탐색 -> 연합 리스트에 추가 -> 그 연합의 인구수를 모두 더함 -> 그 연합의 모든 국가의 수를 평균내서 적용 
# 탐색 : 그냥 for문 돌려서 상하좌우로 탐색. visited같이 방문처리를 해서 중복안되게 하고 다음 연산들에서 사용
# 리스트에 추가 : 연합이 한 덩어리가 아닐 수 있는데, 이러면 연합 리스트를 2차원 리스트를 만들어서 조건 부합했을 때 visited에 있는 곳이라면
# 고 연합에 끼고 없다면 새로운 연합을 만들도록 
# 연합 인구수 더하기 : dfs도 쓰지말고 애초에 리스트에 더할때 인구수까지 튜플로 같이 받자.
# 수정 : dfs를 쓰지 않고 리스트에 추가하는 방식으로는 하나가 추가됐을때 서로 다른 연합 그룹이 연결될 수 있는데, 이를 해결할 수 없다.
# 평균내서 적용 : 해당 연합의 좌표에 평균내서 다 적용
# Recursion 오류 난다. 재귀의 깊이가 너무 깊은가? 그럼 bfs로 해야하나?
# bfs로 했는데 한 4%쯤에서 틀렸다. 반례가 뭐지
# 아 인접한 서로 다른 연합도 하나의 연합으로 판정되네
from collections import deque
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(x,y):
    q = deque()
    visited[x][y] = True
    q.append((x,y))
    alliance = [(x, y)]
    total_pop = mapp[x][y]
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and L <= abs(mapp[cx][cy] - mapp[nx][ny]) <= R:
                q.append((nx,ny))
                visited[nx][ny] = True
                alliance.append((nx,ny))
                total_pop += mapp[nx][ny]
    if len(alliance) > 1:
        new_pop = total_pop // len(alliance)
        for i, j in alliance:
            mapp[i][j] = new_pop
        return True
    return False





N, L, R = map(int,input().split())

mapp = [list(map(int,input().split())) for _ in range(N)]

day = 0

while True:
    visited = [[False]*N for _ in range(N)]
    done = True
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                if bfs(i,j):
                    done = False
                
    if done:
        break
    day += 1
    
print(day)



