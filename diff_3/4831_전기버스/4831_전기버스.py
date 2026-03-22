#13
def solve(mapp):
    cur = 0
    cnt = 0
    while cur < N-K:
        flag = False
        for i in range(K,0,-1):
            if cur + i in mapp:
                cur = cur + i
                cnt += 1
                flag = True
                break
        if not flag:
            return 0 

        
    return cnt

T = int(input())

for i in range(T):
    K,N,M = map(int, input().split())
    mapp = list(map(int,input().split()))
    print(f"#{i+1} {solve(mapp)}")