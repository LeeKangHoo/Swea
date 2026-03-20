dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def move(mapp, d):
    new_mapp = [row[:] for row in mapp]
    merged = [[False] * N for _ in range(N)]
    
    if d == 0 or d == 2:
        range_i = range(N)
        range_j = range(N)
    else:
        range_i = range(N - 1, -1, -1)
        range_j = range(N - 1, -1, -1)
        
    for i in range_i:
        for j in range_j:
            if new_mapp[i][j] == 0:
                continue
                
            x, y = i, j
            while True:
                nx = x + dx[d]
                ny = y + dy[d]
                
                if 0 <= nx < N and 0 <= ny < N:
                    if new_mapp[nx][ny] == 0:
                        new_mapp[nx][ny] = new_mapp[x][y]
                        new_mapp[x][y] = 0
                        x, y = nx, ny
                    elif new_mapp[nx][ny] == new_mapp[x][y] and not merged[nx][ny]:
                        new_mapp[nx][ny] *= 2
                        new_mapp[x][y] = 0
                        merged[nx][ny] = True
                        break
                    else:
                        break
                else:
                    break
    return new_mapp

def solve(mapp, cnt):
    if cnt == 5:
        max_val = 0
        for row in mapp:
            for val in row:
                if val > max_val:
                    max_val = val
        return max_val
        
    res = 0
    for i in range(4):
        next_mapp = move(mapp, i)
        val = solve(next_mapp, cnt + 1)
        if val > res:
            res = val
            
    return res

N = int(input())
mapp = [list(map(int, input().split())) for _ in range(N)]

print(solve(mapp, 0))