#51
from collections import deque
def solve(cur):
    global number
    if cur <= N:
        solve(cur * 2)

        graph[cur] = number
        number += 1
        solve(cur * 2 + 1)
    


T = int(input())

for i in range(T):
    N = int(input())
    graph = [0 for _ in range(N+1)]
    number = 1
    solve(1)
    
    print(f"#{i+1} {graph[1]} {graph[N//2]}")