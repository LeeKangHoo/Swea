#65
# dfs문제 같은데 백트래킹까지 써서 모든 경우를 돌려보는게 좋을 것 같다.
# visited는 필요없음 (어차피 day는 계속 증가)
# 머리 꼬여서 다시 풀기 36분부터


def dfs(d,money,cal):
    global max_val
    max_val = max(max_val,money)

    for next in range(N-d+1):
        if d+cal[d+next][0]+ next <= N+1:
            dfs(d+next+cal[d+next][0],money+cal[d+next][1],cal)
    return
    




N = int(input())
cal = [(0,0)]
# visited = [False for _ in range(N+1)]
max_val = 0

for i in range(N):
    t1,t2 = map(int,input().split())
    cal.append((t1,t2))

for i in range(1,N+1):
    if cal[i][0] + i <= N+1:
        dfs(cal[i][0]+i,cal[i][1],cal)
    

print(max_val)