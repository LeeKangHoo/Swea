# 52
dy = [-1,1]
def solve(x,y):
    ny = y
    while x != 99:
        f = True
        for a in range(2):
            if f:
                ny = dy[a] + y
                if 0 <= ny < 100 and mapp[x][ny] == 1:
                    True
                    while True:
                        ny += dy[a]
                        if 0<= ny < 100 and mapp[x][ny]:
                            continue
                        y = ny - dy[a]
                        f = False
                        break
        x += 1
    
    if mapp[x][y] == 2:
        return True
    else:
        return False
    
for _ in range(10):
    tc = int(input())

    mapp = [list(map(int,input().split())) for _ in range(100)]
    start = []
    for i in range(100):
        if mapp[0][i] == 1:
            start.append(i)
    
    for i in start:
        if solve(1,i):
            print(f"#{tc} {i}")
        
    