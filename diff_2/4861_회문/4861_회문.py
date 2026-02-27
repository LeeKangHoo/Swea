#25
def solve(N,M,mapp):
    r_mapp = list(map(list,zip(*mapp)))

    for row in range(N):    
        for i in range(N-M+1):
            if mapp[row][i:i+M] == mapp[row][i:i+M][::-1]:
                return mapp[row][i:i+M]
            if r_mapp[row][i:i+M] == r_mapp[row][i:i+M][::-1]:
                return r_mapp[row][i:i+M]


T = int(input())

for i in range(T):
    N,M = map(int,input().split())
    mapp = [list(input().strip()) for _ in range(N)]
    r = ''.join(solve(N,M,mapp))
    print(f"#{i+1} {r}")