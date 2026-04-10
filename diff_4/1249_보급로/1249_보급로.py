# 24
# Dijkstra 알고리즘 문제네
# 
import heapq

def solve():
    pq = [(0,0,0)]
    visited[0][0] = 0

    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    while pq:
        cd, cx, cy = heapq.heappop(pq)
        if cx == N-1 and cy == N-1:
            return cd
        if cd > visited[cx][cy]:
            continue
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                dist = cd + mapp[nx][ny]
                if dist < visited[nx][ny]:
                    visited[nx][ny] = dist
                    heapq.heappush(pq,(dist,nx,ny))
    return -1

            

C = int(input())

for tc in range(C):
    N = int(input())
    mapp = [list(map(int,input())) for _ in range(N)]
    visited = [[float('inf')] * N for _ in range(N)]
    print(f"#{tc+1} {solve()}")
