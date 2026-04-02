#1시간 30분 초과X
# mod연산을 통해서 푸는 문제 같다.
# 슬라이싱으로 되나?
# for 문으로 안하고 슬라이싱으로 해야겠다. 꼬인다.
# 아 문제 잘못읽었다
def moving(x,d):
    
    # 시계 방향
    if d == 1:
        tmp = tnbk[x][-1]
        tnbk[x][1:] = tnbk[x][:-1]
        tnbk[x][0] = tmp
    
    # 반 시계 방향
    elif d == -1:
        tmp = tnbk[x][0]
        tnbk[x][:-1] = tnbk[x][1:]
        tnbk[x][-1] = tmp
    return


def solve():
    for i in range(K):
        cx, d = cmd[i]
        cx -= 1
        r = [0]*4
        r[cx] = d
        for t in range(1,4):
            ni, nd = cx+t, cx-t
            if 0 <= ni < 4 and (int(tnbk[ni-1][2]) + int(tnbk[ni][6]))%2 == 1:
                r[ni] = -(r[ni-1])
            if 0 <= nd < 4 and (int(tnbk[nd+1][6]) + int(tnbk[nd][2]))%2 == 1:
                r[nd] = -(r[nd+1])
        
        for t in range(4):
            moving(t,r[t])

    r = 0
    for i in range(4):
        if tnbk[i][0] == 1:
            r += 2**i
    return r


tnbk = [list(map(int,input())) for _ in range(4)]
K = int(input())

cmd = [list(map(int,input().split())) for _ in range(K)]

print(solve())