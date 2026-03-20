#28

def solve():
    mid = N // 2
    r = sum(mapp[mid])
    
    for i in range(mid):
        r += sum(mapp[i][mid-i:mid+i+1])
        r += sum(mapp[N-1-i][mid-i:mid+i+1])
    
    return r
    




T = int(input())

for i in range(T):
    N = int(input())
    mapp = []
    for j in range(N):
        mapp.append(list(map(int,input())))
    print(f"#{i+1} {solve()}")