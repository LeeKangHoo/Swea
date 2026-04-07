#
# 그냥 dfs문제인데 min_val을써서 조기종료 시키면 더 좋겠다
# min_val 초기화 값은 10 ** 6(N최대 100, H최대 1000)
# 시간초과 뜬다 10/4
# 조기종료가 동작 안하나? 잘 동작하는데.....
# 기존에 있는 조기 종료 로직을 더 효율적으로 동작하게 하려면 최대한 빨리 더 낮은 값을 min_val에 찍어줘야하는데
# 아 내려갈때는 연료가 더 안드네? 해결해도 여전히 시간초과에 10/4..

import heapq

def solve():
    visited = [[float('inf')]*N for _ in range(N)]
    visited[0][0] = 0

    pq = [(0,0,0)]
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    while pq:
        d,x,y = heapq.heappop(pq)

        for i in range(4):
            nx,ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                cost = 1
                if mapp[nx][ny] > mapp[x][y]:
                    cost += mapp[nx][ny] - mapp[x][y]
                if visited[nx][ny] > d + cost:
                    visited[nx][ny] = d + cost
                    heapq.heappush(pq,(visited[nx][ny],nx,ny))
    return visited[N-1][N-1]

T = int(input())
for tc in range(T):
    N = int(input())
    mapp = [list(map(int,input().split())) for _ in range(N)]
    
    print(f"#{tc+1} {solve()}")