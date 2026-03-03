#
def solve(grid):
    r_grid = list(map(list,zip(*grid)))
    cnt1 = 0
    cnt2 = 0
    
    if H == 1 and W == 1:
        if grid[0][0] == '.':
            return 1
        else:
            return 0

    for n in range(H):
        if '.' not in grid[n]:
            cnt1 += 1
    
    for n in range(W):
        if '.' not in r_grid[n]:
            cnt2 += 1

    return cnt1 + cnt2

T = int(input())

for i in range(T):
    H, W = map(int,input().split())
    # grid = [['0' for _ in range(W)] for _ in range(H)]
    grid = []

    for j in range(H):
        grid.append(list(input()))
    
    print(solve(grid))