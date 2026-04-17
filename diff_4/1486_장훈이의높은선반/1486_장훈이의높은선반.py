# 30
# 키가 낮은 순서대로 돌려야한다 즉, 다익스트라 알고리즘을 이용해야한다.
# DP로도 할 수 있으려나?
# 어차피 다 돌아야 해서 다익스트라가 아닌가?
# 이전의 조합은 필요없기때문에 idx이용한다.
# 어차피 idx로 다 걸러져서 visited도 필요없다.

import heapq
from collections import deque

def solve(cnt,idx):
    global min_val
    if cnt >= B:
        min_val = min(min_val,cnt-B)
        return
    if idx == N:
        return
    
    for next in range(idx,N):
        solve(cnt+people[next],next+1)
    return


T = int(input())

for tc in range(T):
    N,B = map(int,input().split())
    people = list(map(int,input().split()))
    min_val = sum(people)

    people.sort()
    solve(0,0)
    print(f'#{tc+1} {min_val}')