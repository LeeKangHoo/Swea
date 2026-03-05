#43
def solve(grid):
    r_grid = list(map(list,zip(*grid)))
    cnt1 = 0
    cnt2 = 0

    for n in range(H):
        if '.' not in grid[n]:
            cnt1 += 1
    
    for n in range(W):
        if '.' not in r_grid[n]:
            cnt2 += 1

    if (cnt1 + cnt2) == (H+W):
        return min(H,W)

    return cnt1 + cnt2

T = int(input())

for i in range(T):
    H, W = map(int,input().split())
    # grid = [['0' for _ in range(W)] for _ in range(H)]
    grid = []

    for j in range(H):
        grid.append(list(input()))
    
    print(solve(grid))