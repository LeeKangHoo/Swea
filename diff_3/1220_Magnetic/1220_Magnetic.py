#29
def search(x,y):
    for i in range(x,N):
        if mapp[i][y] == '2':
            return i
    
    return -1


def solve(mapp):
    cnt = 0
    for i in range(N):
        cur = 0
        while cur < N:
            if mapp[cur][i] == '1':
                cur = search(cur,i)
                if cur == -1:
                    break
                else:
                    cnt += 1
            cur += 1
    return cnt
                



for i in range(10):
    N = int(input())
    mapp = [list(input().split()) for _ in range(N)]
    print(f"#{i+1} {solve(mapp)}")
