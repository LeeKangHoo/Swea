# X
# 이거 그냥 가능한 경우의 수를 구하는건데 idx쓴 dfs아닌가
# 70/0 제한시간 초과
# DP문제인가 이거?

# def dfs(idx,cs):
#     if cs not in r:
#         r.add(cs)
#     for i in range(idx,N):
#         dfs(i+1,cs+scores[i])
#     return



T = int(input())

for tc in range(T):
    N = int(input())
    scores = list(map(int,input().split()))
    cnt = 0
    r = {0}

    for s in scores:
        r |= {x + s for x in r}

    # dfs(0,0)
    
    print(f'#{tc+1} {len(r)}')