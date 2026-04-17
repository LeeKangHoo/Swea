# X
# 구현해야하는 로직
# 1. 미세먼지 확산
# 2. 바람 순환
# 바람 이동. 다음 경로에 미세먼지가 있으면 현재 바람의 미세먼지와 합침. 
# 2중 for문으로 하나하나 체크하면서 미세먼지가 5 이상이면 확산시키는 함수 실행 (확산될 때 이미 그 자리에 미세먼지가 있으면 더해지나? 그렇겠네)
# T초 만큼 for문으로 돌리고, 그 안에 2중 for문으로 하나하나 체크하면서 미세먼지가 5 이상이면 확산시키는 함수 실행
# 바람이 계속 나오나?
# deque가 필요하다. 선입 선출이 필요해

from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]
def plt():
    added_dust =[[0]*C for _ in range(R)]
    for px in range(R):
        for py in range(C):
            if room[px][py] >= 5:
                calc_val = room[px][py] // 5
                cnt = 0
                for d in range(4):
                    nx, ny = px + dx[d], py + dy[d]
                    if 0 <= nx < R and 0 <= ny < C and room[nx][ny] != -1:
                        added_dust[nx][ny] += calc_val
                        cnt += 1
                room[px][py] -= calc_val * cnt
    for r in range(R):
        for c in range(C):
            room[r][c] += added_dust[r][c]
    return

def wind():
    # 위쪽 공기청정기 (반시계) 
    up = air[0][0]
    u_path = []
    for c in range(1, C): u_path.append((up, c))          # 우
    for r in range(up - 1, -1, -1): u_path.append((r, C - 1)) # 상
    for c in range(C - 2, -1, -1): u_path.append((0, c))    # 좌
    for r in range(1, up): u_path.append((r, 0))          # 하
    
    # 뒤에서부터 당기기
    for i in range(len(u_path)-1, 0, -1):
        curr_r, curr_c = u_path[i]
        prev_r, prev_c = u_path[i-1]
        room[curr_r][curr_c] = room[prev_r][prev_c]
    room[u_path[0][0]][u_path[0][1]] = 0 # 청정기 직후는 0

    # 아래쪽 공기청정기
    down = air[1][0]
    d_path = []
    for c in range(1, C): d_path.append((down, c))        # 우
    for r in range(down + 1, R): d_path.append((r, C - 1))  # 하
    for c in range(C - 2, -1, -1): d_path.append((R - 1, c)) # 좌
    for r in range(R - 2, down, -1): d_path.append((r, 0))   # 상
    
    # 뒤에서부터 당기기
    for i in range(len(d_path)-1, 0, -1):
        curr_r, curr_c = d_path[i]
        prev_r, prev_c = d_path[i-1]
        room[curr_r][curr_c] = room[prev_r][prev_c]
    room[d_path[0][0]][d_path[0][1]] = 0

R,C,T = map(int,input().split())

room = [list(map(int,input().split())) for _ in range(R)]
widx = deque()
air = []
for i in range(R):
    for j in range(C):
        if room[i][j] == -1:
            air.append((i,j))
            # widx.append((i,j,0))

for _ in range(T):
    # widx.append([(air[0][0],air[0][1]+1,room[air[0][0]][air[0][1]+1]),(air[1][0],air[1][1]+1,room[air[1][0]][air[1][1]+1])])
    widx.append([(air[0][0],air[0][1],1),(air[1][0],air[1][1],1)])
    plt()
    wind()

cnt = 0
for r in range(R):
    for c in range(C):
        if 0 < room[r][c]:
            cnt += room[r][c]
print(cnt)
            