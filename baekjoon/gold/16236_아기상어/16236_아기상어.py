# X
# 상어보다 큰 물고기가 있는 칸은 지나갈 수 없다.
# 크기가 같으면 지나갈순 있지만 먹을 수 없다.
# 상어의 현재 먹은 상태를 exp로 두자. 게임을 예시로 들면 될 것 같다.
# 공간을 주기적으로 체크해서 상어가 먹을 수 있는 것을 찾아야할 것 같다. 왼쪽 위가 우선이니까 그냥 for문 돌려서 상어보다 작으면 eatable리스트에 다 넣어버리고
# eatalbe리스트에 추가하기.
# 가장 가까운 순서대로 체크하는법은 sort를 쓰는 것 같은데, python이 기본으로 제공하는 sort가 기존 리스트에서 순서를 그대로 지킬까? quick sort인가?
# sort도 튜플 가장 첫 번째의 값을 기준으로 하니까 그 점 유의하기.
# 근데 중간에 큰 물고기에 막혀서 못가는 경우가 있잖아? 그럼 그냥 bfs를 돌려서 최대한 가까운걸 찾는게 맞겠네
# 근데 제한시간이 2초라 좀 아슬아슬해보인다.
# 아니지 거리가 가장 가까운 물고기를 "먹으러 간다"니까 그런건 생각 안하네
# 가장 가까운 우선순위를 못먹을 때, 차순위를 먹으러가야하네.
# 막혀서 계속 못갈때도 생각해야해
# 그냥 in 으로 해서 가능한 물고기중 하나로 봐야겠다.
# 그게 아니라 bfs를 가장 거리가 짧은 먹이의 좌표를 구하는데에 쓰고 그냥 xy 갱신하면 되네
# 시간초과 뜨는데 마지막 생각한 로직이 틀렸나보다. bfs를 몇번씩이나 똑같이 돌려서 그런듯 차라리 한 번 돌려서 각 좌표별 실제 거리를 계산하면
# 시간복잡도가 훨씬 나을까?
from collections import deque
dx = [-1,0,1,0]
dy = [0,-1,0,1]
def check(lv,x,y):
    tmp = []
    for i in range(N):
        for j in range(N):
            if 0 < mapp[i][j] < lv:
                d = abs(x-i) + abs(y-j)
                tmp.append((i,j))
    return tmp

def bfs(x,y,lv):
    q = deque()
    visited = [[0] * N for _ in range(N)]
    q.append((x,y))
    r = []
    while q:
        cx, cy = q.popleft()
        if 0 < mapp[cx][cy] < lv:
            r.append((visited[cx][cy],cx,cy))
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N and mapp[nx][ny] <= lv and visited[nx][ny] == 0:
                visited[nx][ny] = visited[cx][cy] + 1
                q.append((nx,ny))
    return r
                
def solve(start):
    lv = 2
    exp = 0
    time = 0
    x,y = start
    mapp[x][y] = 0
    while True:
        
        c = bfs(x,y,lv)
        c.sort()
        
        if len(c) == 0:
            return time
        
        x,y = c[0][1], c[0][2]
        mapp[x][y] = 0
        time += c[0][0]
        exp += 1
        if exp >= lv:
            exp %= lv
            lv += 1
        
# while True:
#         state = check(lv,x,y)
#         if state:    
#             tmp = move(x,y,lv,state)
#             if tmp[-1]:
#                 mapp[x][y] = 0
#                 x,y,time = tmp[0],tmp[1],time+tmp[2]
#                 exp += 1
#                 mapp[x][y] = 9
#                 if exp >= lv:
#                     exp %= lv
#                     lv += 1
#         else:
#             return time
    



N = int(input())

mapp = [list(map(int,input().split())) for _ in range(N)]
f = False
start = (0,0)
for i in range(N):
    if f:
        break
    for j in range(N):
        if mapp[i][j] == 9:
            start = (i,j)
            f = True
            break

print(solve(start))





# #
# # 상어보다 큰 물고기가 있는 칸은 지나갈 수 없다.
# # 크기가 같으면 지나갈순 있지만 먹을 수 없다.
# # 상어의 현재 먹은 상태를 exp로 두자. 게임을 예시로 들면 될 것 같다.
# # 공간을 주기적으로 체크해서 상어가 먹을 수 있는 것을 찾아야할 것 같다. 왼쪽 위가 우선이니까 그냥 for문 돌려서 상어보다 작으면 eatable리스트에 다 넣어버리고
# # eatalbe리스트에 추가하기.
# # 가장 가까운 순서대로 체크하는법은 sort를 쓰는 것 같은데, python이 기본으로 제공하는 sort가 기존 리스트에서 순서를 그대로 지킬까? quick sort인가?
# # sort도 튜플 가장 첫 번째의 값을 기준으로 하니까 그 점 유의하기.
# # 근데 중간에 큰 물고기에 막혀서 못가는 경우가 있잖아? 그럼 그냥 bfs를 돌려서 최대한 가까운걸 찾는게 맞겠네
# # 근데 제한시간이 2초라 좀 아슬아슬해보인다.
# # 아니지 거리가 가장 가까운 물고기를 "먹으러 간다"니까 그런건 생각 안하네
# # 가장 가까운 우선순위를 못먹을 때, 차순위를 먹으러가야하네.
# # 막혀서 계속 못갈때도 생각해야해
# # 그냥 in 으로 해서 가능한 물고기중 하나로 봐야겠다.
# from collections import deque
# dx = [-1,0,1,0]
# dy = [0,1,0,-1]
# def check(lv,x,y):
#     tmp = []
#     for i in range(N):
#         for j in range(N):
#             if 0 < mapp[i][j] < lv:
#                 d = abs(x-i) + abs(y-j)
#                 tmp.append((d,i,j))
#     return sorted(tmp)

# def move(x,y,lv,tx,ty):
#     q = deque()
#     visited = [[0] * N for _ in range(N)]
#     q.append((x,y))

#     while q:
#         cx, cy = q.popleft()
#         if cx == tx and cy == ty:
#             return cx,cy,visited[cx][cy],True
#         for i in range(4):
#             nx = cx + dx[i]
#             ny = cy + dy[i]
#             if 0 <= nx < N and 0 <= ny < N and mapp[nx][ny] <= lv and visited[nx][ny] == 0:
#                 visited[nx][ny] = visited[cx][cy] + 1
#                 q.append((nx,ny))
#     return cx,cy,visited[cx][cy],False
                
# def solve(start):
#     lv = 2
#     exp = 0
#     time = 0
#     x,y = start
#     while True:
#         state = check(lv,x,y)
#         if state:
#             for td,tx,ty in state:
#                 tmp = move(x,y,lv,tx,ty)
#                 if tmp[-1]:
#                     mapp[x][y] = 0
#                     x,y,time = tmp[0],tmp[1],time+tmp[2]
#                     exp += 1
#                     mapp[x][y] = 9
#                     if exp >= lv:
#                         exp %= lv
#                         lv += 1
#                     break
#         else:
#             return time
    



# N = int(input())

# mapp = [list(map(int,input().split())) for _ in range(N)]
# f = False
# start = (0,0)
# for i in range(N):
#     if f:
#         break
#     for j in range(N):
#         if mapp[i][j] == 9:
#             start = (i,j)
#             f = True
#             break

# print(solve(start))