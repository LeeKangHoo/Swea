#X

d = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def solve(pan):
    for x,y,b in command:
        x -= 1
        y -= 1
        pan[x][y] = b
        target = 0
        if b == 1:
            target = 2
        else:
            target = 1

        for i in range(8):
            nx,ny = x + d[i][0], y + d[i][1]
            to_flip = []
            while 0 <= nx < N and 0 <= ny <N:
                if pan[nx][ny] == target:
                    to_flip.append((nx,ny))
                elif pan[nx][ny] == b:
                    for fx,fy in to_flip:
                        pan[fx][fy] = b
                    break
                else:
                    break
                nx,ny = nx + d[i][0], ny + d[i][1]

    w_cnt, b_cnt = 0,0
    for i in range(N):
        b_cnt += pan[i].count(1)
        w_cnt += pan[i].count(2)
    
    return f'{b_cnt} {w_cnt}'
            


T = int(input())

for tc in range(T):
    N,M = map(int,input().split())
    pan = [[0]*N for _ in range(N)]

    
    pan[N//2][N//2] = 2
    pan[N//2-1][N//2-1] = 2
    pan[N//2][N//2-1] = 1
    pan[N//2-1][N//2] = 1
    
    command = [list(map(int,input().split())) for _ in range(M)]

    print(f"#{tc+1} {solve(pan)}")

