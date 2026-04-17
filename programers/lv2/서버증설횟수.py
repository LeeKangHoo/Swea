# 26
# 각 증설한 서버마다 각각 언제 끝나는지 표시 해야함. 
from collections import deque

def solution(players, m, k):
    cur = m
    cnt = 0
    server = deque()
    try:
        for i,p in enumerate(players):
            while p >= cur:
                cur += m
                cnt += 1
                server.append(i+k-1)
                print(f'idx :{i} 현재 수용가능 {cur-1}. 현재 인원{p}, 서버 대여. {i+k-1}에 종료')
            while server and i == server[0]:
                server.popleft()
                cur -= m
                print(i,'에 서버 대여 끝')
    except Exception as e:
        return list(server),i,k,str(e)
    return cnt
            
    
    