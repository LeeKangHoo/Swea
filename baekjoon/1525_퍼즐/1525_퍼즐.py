#X
from collections import deque

def bfs(mapp):
    q = deque()
    visited = set()
    visited.add(mapp)
    q.append((mapp,0))
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    answer = '123456780'
    while q:
        cur_mapp,cnt = q.popleft()
        if cur_mapp == answer:
            return cnt
        z_index = cur_mapp.index('0')
        cx, cy = z_index // 3, z_index % 3
        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            next_mapp = list(cur_mapp)
            if 0 <= nx < 3 and 0 <= ny < 3:
                next_index = nx * 3 + ny
                next_mapp[z_index], next_mapp[next_index] = next_mapp[next_index], next_mapp[z_index]
                next_state = ''.join(next_mapp)
                if next_state not in visited:
                    visited.add(next_state)
                    q.append((next_state, cnt+1))
    return -1


mapp = ''

for i in range(3):
    mapp += ''.join(input().split())

print(bfs(mapp))