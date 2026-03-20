#16
def solve(mapp):
    cnt = 0
    for i in range(8):
        for j in range(8-N+1):
            if mapp[i][j:j+N] == mapp[i][j:j+N][::-1]:
                cnt += 1
    
    mapp_r = list(map(list,zip(*mapp)))

    for i in range(8):
        for j in range(8-N+1):
            if mapp_r[i][j:j+N] == mapp_r[i][j:j+N][::-1]:
                cnt += 1
    return cnt


for tc in range(10):
    N = int(input())
    mapp = []
    for i in range(8):
        mapp.append(input())

    print(f"#{tc+1} {solve(mapp)}")