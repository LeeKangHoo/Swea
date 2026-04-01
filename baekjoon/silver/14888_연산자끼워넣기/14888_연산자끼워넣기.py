#X
# dfs로 모든 경우를 돌아보는 것 같다.
# 처음에 하다보니 단순 for문으로 만들었는데 너무 복잡해서 dfs로 재귀를 제대로 써봐야겠다.
# set을 써볼까? (no)
# 소모형식으로 해볼까?
def calc(cmds,nums):
    n = nums[0]
    t_nums = nums[1:]
    for i in range(N-1):
        if cmds[i] == 0:
            n += t_nums[i]
        elif cmds[i] == 1:
            n -= t_nums[i]
        elif cmds[i] == 2:
            n *= t_nums[i]
        elif cmds[i] == 3:
            n /= t_nums[i]
        else:
            print("error")
    return n
def dfs(idx,total,cmd):
    global max_val,min_val

    if idx == N:
        max_val = max(max_val,total)
        min_val = min(min_val,total)
    

    if cmd[0] > 0:
        cmd[0] -= 1
        dfs(idx+1, total + nums[idx], cmd)
        cmd[0] += 1

    if cmd[1] > 0:
        cmd[1] -= 1
        dfs(idx+1, total - nums[idx], cmd)
        cmd[1] += 1
    
    if cmd[2] > 0:
        cmd[2] -= 1
        dfs(idx+1, total * nums[idx], cmd)
        cmd[2] += 1
    
    if cmd[3] > 0:
        cmd[3] -= 1
        dfs(idx+1, int(-(-(total)/nums[idx])), cmd)
        cmd[3] += 1

    return


            
            
    
            
    


    # global max_val,min_val
    # cmds = [-1] * (N-1)

    # for plus in range(cmd[0]):
    #     for i in range(N-1):
    #         if not visited[i][0] and cmds[i] == -1:
    #             cmds[i] = 0
    #             visited[i][0] = True
    #         for minus in range(cmd[1]):
    #             for i in range(N-1):
    #                 if not visited[i][1] and cmds[i] == -1:
    #                     cmds[i] = 1
    #                     visited[i][1] = True
    #             for multi in range(cmd[2]):
    #                 for i in range(N-1):
    #                     if not visited[i][2] and cmds[i] == -1:
    #                         cmds[i] = 2          
    #                         visited[i][2] = True         
    #                 for mod in range(cmd[3]):
    #                     for i in range(N-1):
    #                         if not visited[i][2] and cmds[i] == -1:
    #                             cmds[i] = 2
    #                             visited[i][3] = True
    #                             tmp = calc(cmds,nums)
    #                             max_val = max(max_val,tmp)
    #                             min_val = min(min_val,tmp)
    #                             visited[i][3] = False
    #                 visited[i][2] = False

# [+ + - * %]
# [+ - + * %]
        

def solve(nums,cmd):
    global max_val, min_val
    max_val = -10**10
    min_val = 10**10
    
    # visited = [[False] * 4 for _ in range(N-1)]
    # cl = [-1]*(N-1)
    # visited = set()

    dfs(1,nums[0],cmd)
    return [max_val,min_val]



    


N = int(input())

nums = list(map(int,input().split()))
cmd = list(map(int,input().split()))

for i in solve(nums,cmd):
    print(i)

