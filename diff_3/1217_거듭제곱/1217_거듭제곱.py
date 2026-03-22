#5
def solve(cur,cnt):
    if cnt == M-1:
        return cur * N
    return solve(cur*N,cnt+1)


for i in range(10):
    tc = int(input())
    N,M = map(int,input().split())

    print(f'#{tc} {solve(N,1)}')