# 8
# +1 -1 *2 -10
# 위 4가지의 연산만 가능한데, 자연수 N에서 M으로 만들려면 최소 몇 번의 연산을 거쳐야 하나?
# 연산의 중간 결과도 항상 1,000,000 이하의 자연수여야 한다.
# 최소 연산이니까 bfs로 해보면 되지 않을까?
# 그리고 set을 써서 이미 왔던 수는 제외시키자
from collections import deque

def calc(cmd,n):
    if cmd == 0:
        tmp = n + 1
        if 0 < tmp <= 1000000:
            return tmp
        return -1
    elif cmd == 1:
        tmp = n -1
        if 0 < tmp <= 1000000:
            return tmp
        return -1
    elif cmd == 2:
        tmp = n*2
        if 0 < tmp <= 1000000:
            return tmp
        return -1
    elif cmd == 3:
        tmp = n - 10
        if 0 < tmp <= 1000000:
            return tmp
        return -1


def solve(N,M):
    visited = {N}
    q = deque()
    q.append((N,0))
    while q:
        cn, cnt = q.popleft()
        if cn == M:
            return cnt
        for i in range(4):
            next = calc(i,cn)
            if next != -1 and next not in visited:
                visited.add(next)
                q.append((next,cnt+1))
    return -1


T = int(input())

for tc in range(T):
    N, M = map(int,input().split())
    
    print(f"#{tc+1} {solve(N,M)}")