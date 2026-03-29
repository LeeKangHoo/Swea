#36

def solve(cur,n,nums,visited):
    global cnt
    visited[n] = True
    if cur == K:
            cnt += 1
            return 
    
    
    for next in range(n+1,N):
        if not visited[next] and nums[next]+cur <= K:
            solve(nums[next]+cur,next,nums,visited)
            visited[next] = False
    return 

    

T = int(input())

for i in range(T):
    N, K = map(int,input().split())
    nums = list(map(int,input().split()))
    visited = [False] * N
    
    cnt = 0

    for a in range(N):
        solve(nums[a],a,nums,visited)
        visited[a] = False

    print(f"#{i+1} {cnt}")