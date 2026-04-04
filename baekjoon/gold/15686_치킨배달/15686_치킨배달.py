# 1시간 30분 초과
# 어떤 좌표에서부터 치킨집까지의 최소거리를 구해서 합을 하기 때문에 BFS
# 폐업을 시키지 않을 치킨집 최대 M개를 골라야한다. 
# 어떻게 고르면 도시의 치킨 거리(치킨거리들의 합)가장 작게될까?
# 그냥 bfs만 돌리면 최소거리의 합이니까 되려나? 어차피 최대 M까지 모두 가능하니까
# 아 무조건 폐업을 시켜야하네 M개만 남기고
# dfs로 어떤 치킨집을 남길지 정하고 bfs로 돌아보기
# 시간 초과? pypy3도 시간초과가 뜬다.
# 아니면 혹시 dfs로 한 번 돌려서 치킨집마다 각 집까지의 거리를 더해서 가장 수가 낮은 것 순서대로 3개 뽑아서 쓰는건가?
# 어차피 거리 계산이면 bfs dfs를 할 필요가 없네?
# 이러지말고 bfs로 가장 가깝게 선택된 횟수를 보면되겠네 다 같을 경우에는 거리 계산으로 정하고

def dfs(idx,cnt):
    global min_val
    if cnt == M:
        tmp = 0
        for hx,hy in house:
            min_tmp = 10**6
            for cx,cy in select:
                r = abs(hx-cx) + abs(hy-cy)
                if r < min_tmp:
                    min_tmp = r
            tmp += min_tmp

        if tmp < min_val:
            min_val = tmp
        return
    

    for i in range(idx,len(chicken)):
        select.append(chicken[i])
        dfs(i+1,cnt+1)
        select.pop()



N,M = map(int,input().split())

mapp = [list(map(int,input().split())) for _ in range(N)]
house = []
chicken = []
for i in range(N):
    for j in range(N):
        if mapp[i][j] == 1:
            house.append((i,j))
        elif mapp[i][j] == 2:
            chicken.append((i,j))
d = [0]*len(chicken)

min_val = 10**6
select = []
dfs(0,0)


print(min_val)