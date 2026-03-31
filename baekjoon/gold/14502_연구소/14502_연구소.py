# X(1시간20분 초과)
# 알고리즘 문제. 로직은 바이러스 움직일거 하나 필요하고 벽 설치하는거 필요
# 벽 설치하는건 그냥 for문 3개 돌려서 해버리고 바이러스 퍼지는 것만 dfs해보는걸로 시도
# 시간초과가 떴다. 아마 모든 벽의 경우의 수를 하지 말고, 차라리 1과 2 근처에만 해봐도 될 것 같다.

# 예제 3번에서 확인해보니 아예 바이러스랑 관련없이 비어있는 구석에 대각선으로 벽을 세우면 3개가 된다. 따라서 두 번째 시도도 실패
# 첫 번째 방식대로 모든 벽의 경우의수를 넣는 대신, 바이러스 로직에서 dfs말고 bfs로 고친 후 조기 종료 로직을 추가하면?
# pypy3으로 돌리면 통과되는데 python3는 시간초과가 여전히 뜬다.


from collections import deque
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def virus(v,min_val):
    visited = [[False] * M for _ in range(N)]
    q = deque()
    cnt = 0
    for x,y in v:
        q.append((x,y))
        visited[x][y] = True
        cnt += 1

    while q:
        if cnt >= min_val:
            return -1
        cx, cy = q.popleft()
        for i in range(4):
            nx = dx[i] + cx
            ny = dy[i] + cy
            if 0 <= nx < N and 0 <= ny < M and mapp[nx][ny] == 0 and not visited[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny] = True
                cnt += 1
    return cnt
    


# def virus(x,y,mapp,visited):
    #dfs 시도 (실패)
    # cnt = 1
    # for i in range(4):
    #     nx = dx[i] + x
    #     ny = dy[i] + y
    #     if 0 <= nx < N and 0 <= ny < M and mapp[nx][ny] == 0 and visited[nx][ny] == 0:
    #         visited[nx][ny] = visited[x][y] + 1
    #         cnt += virus(nx,ny,mapp,visited)
    # return cnt

def solve(mapp):
    max_val = 0
    min_val = N*M
    wall = 3
    
    v = []
    empty = []
    for i in range(N):
        for j in range(M):
            if mapp[i][j] == 2:
                v.append((i,j))
            elif mapp[i][j] == 1:
                wall += 1
            else:
                empty.append((i,j))
    for i in range(len(empty)):
        for j in range(i+1,len(empty)):
            for z in range(j+1,len(empty)):
                x1, y1 = empty[i]
                x2, y2 = empty[j]
                x3, y3 = empty[z]
                mapp[x1][y1] = 1
                mapp[x2][y2] = 1
                mapp[x3][y3] = 1
                
                sum_val = virus(v,min_val)
                if sum_val != -1:
                    min_val = sum_val
                    max_val = max(max_val,(N*M) - (sum_val + wall))                

                mapp[x1][y1] = 0
                mapp[x2][y2] = 0
                mapp[x3][y3] = 0
    
    return max_val


    # 세 번째 시도(bfs로 바꾸고 조기 종료)
    # max_val = 0
    # min_val = N*M
    # wall = 3
    
    # v = []
    # for i in range(N):
    #     for j in range(M):
    #         if mapp[i][j] == 2:
    #             v.append((i,j))
    #         elif mapp[i][j] == 1:
    #             wall += 1
    # for a in range(N):
    #     for b in range(M):
    #         if mapp[a][b] == 0:
    #             mapp[a][b] = 1
    #             for x in range(N):
    #                 for y in range(M):
    #                     if mapp[x][y] == 0:
    #                         mapp[x][y] = 1
    #                         for i in range(N):
    #                             for j in range(M):
    #                                 if mapp[i][j] == 0:
    #                                     sum_val = virus(v,min_val)
    #                                     if sum_val != -1:
    #                                         min_val = sum_val
    #                                         max_val = max(max_val,(N*M) - (sum_val + wall))
                                        
    #                                     mapp[i][j] = 0
    #                         mapp[x][y] = 0
    #             mapp[a][b] = 0
    # return max_val

    
    # 두 번째 시도(벽과 바이러스 근처만 벽 설치)
    # wall = []
    # v = []
    # max_val = 0
    # wall_cnt = 3
    # # 벽과 바이러스 위치 기록
    # for i in range(N):
    #     for j in range(M):
    #         if mapp[i][j] == 1:
    #             wall_cnt += 1
    #             wall.append((i,j))
    #         elif mapp[i][j] == 2:
    #             v.append((i,j))
                

    # wx = [-1,-1,0,1,1,1,0,-1]
    # wy = [0,1,1,1,0,-1,-1,-1]
    # can = set()
    
    # # 벽 주변 좌표 기록
    # for cwx,cwy in wall:
    #     for i in range(8):
    #         nwx = cwx + wx[i]
    #         nwy = cwy + wy[i]
    #         if 0 <= nwx < N and 0 <= nwy < M and mapp[nwx][nwy] == 0:
    #             can.add((nwx,nwy))
    # # 바이러스 주변 좌표 기록
    # for cvx, cvy in v:
    #     for i in range(8):
    #         nvx = cvx + wx[i]
    #         nvy = cvy + wy[i]
    #         if 0 <= nvx < N and 0 <= nvy < M and mapp[nvx][nvy] == 0:
    #             can.add((nvx,nvy))

    # for ax,ay in can:
    #     mapp[ax][ay] = 1
    #     for bx,by in can:
    #             if mapp[bx][by] == 0:
    #                 mapp[bx][by] = 1
    #                 for cx, cy in can:
    #                     if mapp[cx][cy] == 0:
    #                         mapp[cx][cy] = 1
    #                         visited = [[0] * M for _ in range(N)]
    #                         sum_val = 0
    #                         for vx,vy in v:
    #                             sum_val += virus(vx,vy,mapp,visited)
    #                         max_val = max(max_val,(N*M) - (sum_val + wall_cnt))
    #                         mapp[cx][cy] = 0
    #                 mapp[bx][by] = 0
    #     mapp[ax][ay] = 0
    # return max_val





    # 첫 시도(모든 벽의 경우의 수를 계산)
    # max_val = 0
    # wall = 3
    
    # v = []
    # for i in range(N):
    #     for j in range(M):
    #         if mapp[i][j] == 2:
    #             v.append((i,j))
    #         elif mapp[i][j] == 1:
    #             wall += 1
    # for a in range(N):
    #     for b in range(M):
    #         if mapp[a][b] == 0:
    #             mapp[a][b] = 1
    #             for x in range(N):
    #                 for y in range(M):
    #                     if mapp[x][y] == 0:
    #                         mapp[x][y] = 1
    #                         for i in range(N):
    #                             for j in range(M):
    #                                 if mapp[i][j] == 0:
    #                                     mapp[i][j] = 1
    #                                     visited = [[0] * M for _ in range(N)]
    #                                     sum_val = 0
    #                                     for vx,vy in v:
    #                                         sum_val += virus(vx,vy,mapp,visited)

    #                                     max_val = max(max_val,(N*M) - (sum_val + wall))
    #                                     mapp[i][j] = 0
    #                         mapp[x][y] = 0
    #             mapp[a][b] = 0
    # return max_val
            


N, M = map(int,input().split())
mapp = [list(map(int,input().split())) for _ in range(N)]

print(solve(mapp))