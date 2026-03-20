#
import sys

def dfs(cur,visited_count,cur_cost):
    global min_cost
    
    if cur_cost > min_cost:
        return
    
    if visited_count == N:
        if mapp[cur][0] != 0:
            min_cost = min(min_cost,cur_cost + mapp[cur][0])
        return
    
    for next in range(N):
        if mapp[cur][next] != 0 and not visited[next]:
            visited[next] = True
            dfs(next,visited_count+1,cur_cost+mapp[cur][next])
            visited[next] = False

    


N = int(input())
mapp = []
min_cost = sys.maxsize

for i in range(N):
    mapp.append(list(map(int,input().split())))
visited = [False] * N
min_size = sys.maxsize
visited[0] = True
dfs(0,1,0)

print(min_cost)
        
