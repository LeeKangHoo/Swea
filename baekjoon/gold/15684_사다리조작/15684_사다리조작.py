# 1시간 30분 초과
# bfs로 하는 것 같다
# 입력받을때 index형태로 받는게 아니라 -1을 다 해줘야한다. 그냥 처음에 해두는게 낫겠다.
# 백트래킹인가? 백트래킹을 꼭 해야하나?
# N == y
# H == x
# M == 그냥 이미 설치되어 있는 가로선
# 불가능 하다는건 i에서 i로 가는게 안되는 경우가 있을 경우인가?  
# 아 하나씩 확인하는게 아니라 전부다 확인이네
# 추가할 가로선의 수를 정해서 3 이상이면 그냥 다 -1 떄려버리면?
# 왜 바로 틀렸지?
# 이유가 없는데?
# 마지막에 - 오타 나서 그랬네, 근데 이젠 시간초과가 뜨네
import sys
input = sys.stdin.readline
def check():
    for cur in range(N):
        c = cur
        for i in range(H):
            if mapp[i][c] == 1:
                c += 1
            elif mapp[i][c] == -1:
                c -= 1
        if c != cur:
            return False
    return True


def solve(x,y,cnt,t):
    global found
    if found:
        return
    if cnt >= min_val or cnt > 3:
        return 
    if cnt == t:
        if check():
            # min_val = min(min_val,cnt)
            found = True
        return 
 

    for i in range(x,H):
        start_y = y if i == x else 0
        for j in range(start_y,N-1):
            if mapp[i][j] == 0 and mapp[i][j+1] == 0:
                mapp[i][j] = 1
                mapp[i][j+1] = -1
                solve(i,j+2,cnt+1,t)
                mapp[i][j] = 0
                mapp[i][j+1] = 0




    # for i in range(N-1):
    #     if mapp[idx][i] == 0:
    #         mapp[idx][i] = 1
    #         mapp[idx][i+1] = -1
    #         solve(idx+1,cnt+1)
    #         mapp[idx][i] = 0
    #         mapp[idx][i+1] = 0

    # 불가능할때 -1 하는거 어떻게 해야할까
    # min_val = -1
    return




N,M,H = map(int,input().split())

mapp = [[0] * N for _ in range(H)]
visited = [[0] * N for _ in range(H)]

for i in range(M):
    b,a = map(int,input().split())
    b -= 1
    a -= 1
    mapp[b][a] = 1
    mapp[b][a+1] = -1
min_val = 4

if check():
    min_val = 0
else:
    found = False

for i in range(1,4):
    solve(0,0,0,i)
    if found:
        min_val = i
        break

if min_val > 3:
    min_val = -1

print(min_val)
