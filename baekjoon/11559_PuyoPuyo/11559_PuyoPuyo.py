#X
from collections import deque

def bfs(x,y,mapp,visited):
    q = deque()
    q.append((x,y))
    visited[x][y] = True 
    P = mapp[x][y]
    
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    bomb_list = [(x,y)]
    
    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx = dx[i] + cx
            ny = dy[i] + cy
            if 0 <= nx < 12 and 0 <= ny < 6 and mapp[nx][ny] == P and visited[nx][ny] == 0:
                visited[nx][ny] = True
                bomb_list.append((nx,ny))
                q.append((nx,ny))

    if len(bomb_list) >= 4:
        for bx,by in bomb_list:
            mapp[bx][by] = '.'
        return True
    else:
        return False

mapp = []


for i in range(12):
    mapp.append(list(input()))

c_cnt = 0
while True:
    visited = [[False] * 6 for _ in range(12)]
    flag = False

    for i in range(12):
        for j in range(6):
            if mapp[i][j] != '.' and not visited[i][j]:
                if bfs(i,j,mapp,visited):
                    flag = True
                
    if not flag:
        break
    c_cnt += 1
                    
    t_mapp = list(map(list,zip(*mapp)))
    for i in range(6):

        blocks = [p for p in t_mapp[i] if p != '.']
        blank = ['.'] * (12 - len(blocks))
        
        t_mapp[i][:] = blank + blocks

    mapp[:] = list(map(list,zip(*t_mapp)))
    

print(c_cnt)
                    
            
