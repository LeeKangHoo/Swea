#X
from collections import deque
import sys
input = sys.stdin.readline


def bfs(A,B):
    q = deque()
    visited = [False] * 10000
    q.append(A)
    visited[A] = True
    command = [''] * 10000
    parent = [-1] * 10000
    while q:
        cur = q.popleft()
        if cur == B:
            path = []
            while cur != A:
                path.append(command[cur])
                cur = parent[cur]
            return ''.join(path[::-1])

        nxt = (cur * 2) % 10000
        if not visited[nxt]:
            visited[nxt] = True
            parent[nxt] = cur
            command[nxt] = 'D'
            q.append(nxt)
            
        nxt = cur - 1 if cur != 0 else 9999
        if not visited[nxt]:
            visited[nxt] = True
            parent[nxt] = cur
            command[nxt] = 'S'
            q.append(nxt)
            
        nxt = (cur % 1000) * 10 + (cur // 1000)
        if not visited[nxt]:
            visited[nxt] = True
            parent[nxt] = cur
            command[nxt] = 'L'
            q.append(nxt)
            
        nxt = (cur % 10) * 1000 + (cur // 10)
        if not visited[nxt]:
            visited[nxt] = True
            parent[nxt] = cur
            command[nxt] = 'R'
            q.append(nxt)

    


T = int(input())
r = []

for i in range(T):
    A, B = map(int,input().split())
    
    r.append(bfs(A,B))

for n in r:
    print(n)