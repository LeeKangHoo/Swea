#X
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x,y):
    visited.add(mapp[x][y])

    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    cnt = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < R and 0 <= ny < C and mapp[nx][ny] not in visited:
            visited.add(mapp[nx][ny])
            cnt = max(cnt, dfs(nx,ny) + 1)
            visited.remove(mapp[nx][ny])
            
    return cnt





R, C = map(int,input().split())
mapp = []
visited = set()

for i in range(R):
    mapp.append(input().strip())

print(dfs(0,0))