#X
from collections import deque
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def bfs():
    q = deque()
    q.append((0,0,0))
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 1

    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    while q:
        cx, cy, w = q.popleft()
        if cx == N-1 and cy == M-1:
            return visited[cx][cy][w]
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if mapp[nx][ny] == '0' and visited[nx][ny][w] == 0:
                    visited[nx][ny][w] = visited[cx][cy][w] + 1
                    q.append((nx,ny,w))
                elif mapp[nx][ny] == '1' and w == 0:
                    visited[nx][ny][1] = visited[cx][cy][0] + 1
                    q.append((nx,ny,1))
    return -1


N, M = map(int,input().split())
mapp = []


for i in range(N):
    mapp.append(list(input().rstrip()))

print(bfs())