#X
from collections import deque
def solve(N):
    visited = [0] * 100001
    q = deque()
    visited[N] = 1
    q.append(N)

    while q:
        cur = q.popleft()  
        if cur == K:
            return visited[cur] - 1
        
        for next in (cur*2,cur+1,cur-1):
            if 0 <= next < 100001 and not visited[next]:
                visited[next] = visited[cur] + 1
                q.append(next)


N, K = map(int, input().split())

print(solve(N))
