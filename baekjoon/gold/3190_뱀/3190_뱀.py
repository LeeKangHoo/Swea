#64
from collections import deque
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def move(x,y,t,d,mapp,q):
    for i in range(t):
            x += dx[d]
            y += dy[d]
            if 0 <= x < N and 0 <= y < N:
                if mapp[x][y] == 2:
                    q.append((x,y))
                    mapp[x][y] = 1
                elif mapp[x][y] == 0:
                    tx,ty = q.popleft()
                    q.append((x,y))
                    mapp[x][y] = 1
                    mapp[tx][ty] = 0
                else:
                    return (-1,i+1,True)
            else:
                return (-1,i+1,True)
    
    return (x,y,False)

    


    
def game(mapp,cmd):
    q = deque()
    q.append((0,0))
    x, y, time, body = 0,0,0,0
    d = 1
    for cl,cd in cmd:
        x,y,flag = move(x,y,int(cl) - time,d,mapp,q)
        if flag:
            return time + y
        else:
            time = int(cl)
            if cd == 'L':
                d = (d+3)%4
            elif cd == 'D':
                d = (d+1)%4

    x,t,flag = move(x,y,100,d,mapp,q)
    
    return time + t




N = int(input())
K = int(input())

mapp = [[0]*N for _ in range(N)]
mapp[0][0] = 1

for i in range(K):
    tx,ty = map(int,input().split())
    mapp[tx-1][ty-1] = 2

L = int(input())
cmd = []
for i in range(L):
    cmd.append((input().split()))

print(game(mapp,cmd))