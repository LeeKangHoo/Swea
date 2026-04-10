# X
# 배열을 뒤집어서 하는게 훨씬 편한가?
# 복도까지 총 3 * 200
# 어떻게 도착지의 위치를 계산하는가? -> 홀수 일때는 v//2 , 짝수일때는 v//2 -1
# 겹치는지 어떻게 알아? -> 출발지와 도착지 사이에 있는 값이 다른 출발지 또는 도착지 값에 있는경우
# 가장 짧은 단위시간 경우는 어떻게 구해? -> dfs, 백트래킹, 조기종료
# 시간은 동시에 1 단위씩 흐르고 한 턴에 모든 학생들의 위치를 연산(이동). 
# 1 단위 시간에는 거리에 상관없이 한번만 흐르고 동선이 겹치면 한 학생만 이동
# solve에선 뭐할거야? -> 겹치는 것들끼리 묶어둔걸로 solve에 넘겨서 먼저 움직여서 다 돌려보고 
# 근데 생각해보니까 어차피 최소를 구하는건데 큰거 하나에 Disjoint set 둘 이상이 묶여있다고 쳐도 그냥 하나 풀린걸 가정하고 하면 되는거 아닌가? 
# 순차적으로 아예 안겹치는거 있는지 확인하고 그건 리스트에서 빼고 cnt += 1하고 다시 거기서 어떤 학생 a를 한번 먼저 보내보고 안겹치면
# a를 리스트에서 빼고 cnt +=1 이런식으로 하면 되지않나?
# 근데 만약 2중 이상으로 묶여있다면? 그걸 dfs로 해야하는구나?
# 10/1 인데?
# 개선을 했는데 10/2에 시간초과네



# 현재 students에서 그냥 지나가도 안겹치는 학생이 있는지 확인해서 인덱스를 포함한 리스트를 반환
# def check():
#     sl = len(students)
#     r = []
#     for i in range(sl):
#         if not visited[i]:
#             s1,d1 = students[i]
#             f = True
#             for j in range(sl):
#                 if i == j:
#                     continue
#                 if not visited[j]:
#                     s2,d2 = students[j]
#                     # 여기 등호도 써야하는지 아닌지 모르겠음
#                     if s1 <= s2 <= d1 or s1 <= d2 <= d1 or s2 <= s1 <= d2 or s2 <= d1 <= d2:
#                         f = False
#                         break
#             if f:
#                 r.append(i)
#     return r

# def dfs(cnt):
#     global min_val
#     if cnt >= min_val:
#         return
#     is_check = check()
#     if is_check:
#         for i in is_check:
#             visited[i] = True
#     if not(False in visited):
#         min_val = min(min_val,cnt)
#         for i in is_check:
#                 visited[i] = False
#         return
#     for i in range(N):
#         if not visited[i]:
#             visited[i] = True
#             dfs(cnt+1)
#             visited[i] = False
#     return
        



T = int(input())

for tc in range(T):
    N = int(input())
    # students = [list(map(int,input().split())) for _ in range(N)]
    # visited = [False] * N
    # room = [[False] * 200 for _ in range(3)]
    # min_val = 10*4
    # c = 1
    # # dfs(c)

    # print(f'#{tc+1} {min_val}')

    corridor = [0] * 201
    mapp = [list(map(int,input().split())) for _ in range(N)]
    for s,e in mapp:
        cs = (s+1) // 2
        ce = (e+1) // 2
        if cs > ce:
            cs, ce = ce, cs
        for i in range(cs,ce+1):
            corridor[i] += 1
        
    print(f'#{tc + 1} {max(corridor)}')

    
    
    
        
