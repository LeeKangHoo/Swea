#
dx = [0,0,-1,1]
dy = [1,-1,0,0]
def solve(mapp,x,y):
    # 이상하게 나오면 여기부터 맞는지 재점검
    # dice = [[6,3,1,4],[2,3,5,4],[1,3,6,4],[5,3,2,4],[2,1,5,6],[2,6,5,4]]

    dice = [0,0,0,0,0,0]
    # [1,3,4,2,5,6]
    # [2,3,4,6,1,5]
    # [3,6,1,2,5,4]
    # [4,1,6,2,5,3]

    # [2,3,4,6,1,5]
    # [3,1,4,2,5,6]
    
    # 4(남쪽)
    # 0 -> dice[dc]
    # 3(dc) -> dice[5]
    # 1,2 -> 그대로(안움직여서)
    # 4(c) -> dice[0]
    # 5 -> dice[c]

    # 1(동쪽)
    # 0 -> dice[c]
    # 2(dc) -> dice[0]
    # 1(c) -> dice[5]
    # 3,4 -> 그대로 (안움직여서)
    # 5 -> C방향의 반대편

    # 2(서쪽)
    # 0 -> dice[c]
    # 1(dc) -> dice[0]
    # 2(c) -> dice[5]
    # 3,4 -> 그대로 (안움직여서)
    # 5 -> C방향의 반대편


    for c in cmd:
        nx = x+ dx[c-1]
        ny = y+ dy[c-1]
        if 0 <= nx < N and 0 <= ny < M:
            x, y = nx, ny
            
            dc = 0
            if c in [1,3]:
                dc = c+1
            else:
                dc = c-1
            
            if c in [1,2]:
                dice[0], dice[dc], dice[c], dice[5] = dice[c], dice[0], dice[5], dice[dc]
            else:
                dice[0], dice[dc], dice[c], dice[5] = dice[dc], dice[5], dice[0], dice[c]
            print(dice[0])

            if mapp[x][y] == 0:
                mapp[x][y] = dice[5]
            else:
                dice[5] = mapp[x][y]
                mapp[x][y] = 0
            
                
# 4(남쪽)
    # 0 -> dice[dc]
    # 3(dc) -> dice[5]
    # 1,2 -> 그대로(안움직여서)
    # 4(c) -> dice[0]
    # 5 -> dice[c]


N,M,x,y,K = map(int,input().split())
mapp = []

for i in range(N):
    mapp.append(list(map(int,input().split())))

cmd = list(map(int,input().split()))
solve(mapp,x,y)