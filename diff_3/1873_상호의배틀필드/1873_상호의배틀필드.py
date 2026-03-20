#X
def solve(x,y,mapp,command):
    while command:
        cur = command[0]
        command = command[1:]
        # dx = [-1,0,1,0]
        # dy = [0,1,0,-1]
        # c = ['U','D','L','R']
        # d = ['^','V','<','>']
        if cur == 'U':
            mapp[x][y] = '^'
            if 0 <= x-1 < r and mapp[x-1][y] == '.':
                mapp[x][y], mapp[x-1][y] = mapp[x-1][y], mapp[x][y]
                x -= 1
        elif cur == 'D':
            mapp[x][y] = 'v'
            if 0 <= x+1 < r and mapp[x+1][y] == '.':
                mapp[x][y], mapp[x+1][y] = mapp[x+1][y], mapp[x][y]
                x += 1
        elif cur == 'L':
            mapp[x][y] = '<'
            if 0 <= y-1 < c and mapp[x][y-1] == '.':
                mapp[x][y], mapp[x][y-1] = mapp[x][y-1], mapp[x][y]
                y -= 1
        elif cur == 'R':
            mapp[x][y] = '>'
            if 0 <= y+1 < c and mapp[x][y+1] == '.':
                mapp[x][y], mapp[x][y+1] = mapp[x][y+1], mapp[x][y]
                y += 1
        elif cur == 'S':
            cd = mapp[x][y]
            if cd == '^':
                for i in range(x-1,-1,-1):
                    if mapp[i][y] == '#':
                        break
                    elif mapp[i][y] == '*':
                        mapp[i][y] = '.'
                        break
            elif cd == 'v':
                for i in range(x+1,r):
                    if mapp[i][y] == '#':
                        break
                    elif mapp[i][y] == '*':
                        mapp[i][y] = '.'
                        break
            elif cd == '<':
                for i in range(y-1,-1,-1):
                    if mapp[x][i] == '#':
                        break
                    elif mapp[x][i] == '*':
                        mapp[x][i] = '.'
                        break
            elif cd == '>':
                for i in range(y+1,c):
                    if mapp[x][i] == '#':
                        break
                    elif mapp[x][i] == '*':
                        mapp[x][i] = '.'
                        break
    

T = int(input())

for i in range(T):
    r,c = map(int,input().split())
    mapp = [list(input()) for _ in range(r)]
    N = int(input())
    command = list(input())
    x,y = 0, 0
    for a in range(r):
        for b in range(c):
            if mapp[a][b] in ['<','>','v','^']:
                x, y = a,b
                break
    solve(x,y,mapp,command)
    print(f"#{i+1} ", end='')
    for b in range(r):
        print(''.join(mapp[b]))