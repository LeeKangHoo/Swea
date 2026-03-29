#31
def solve():
    if N == 1:
        if d[0] >= M:
            return 'Possible'
        else:
            return 'Impossible'
        
    cur = 0
    m = 0
    for i in range(N):
        m += 1
        cur += (d[i] // M) * K - m
        if cur < 0:
            return 'Impossible'
    
    return "Possible"

T = int(input())

for i in range(T):
    N,M,K = map(int,input().split())
    d = list(map(int,input().split()))
    d.sort()
    print(f"#{i+1} {solve()}")