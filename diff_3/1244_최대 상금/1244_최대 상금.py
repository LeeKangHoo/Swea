#105
def dfs(cnt):
    global max_num

    state = ("".join(number), cnt)
    if state in visited:
        return
    visited.add(state)


    if cnt == 0:
        cur_num = int("".join(number))
        max_num = max(max_num,cur_num)
        return

    for i in range(len(number)):
        for j in range(i+1,len(number)):
            number[i], number[j] = number[j], number[i]
            dfs(cnt - 1)
            number[i], number[j] = number[j], number[i]
    
T = int(input())

for i in range(T):
    number,N = input().split()
    N = int(N)
    number = list(number)
    max_num = 0
    visited = set()
     
    dfs(N)
    print(f"#{i+1} {max_num}")






    #cnt = N
    # z = N - 1
    # while cnt > 0:
    # for z in range(N-1,-1,-1):
    #     if cnt > 0:
    #         change_flag = False
    #         max_val = 0
    #         max_idx = 0
    #         for x in range(len(number)-1,z,-1):
    #             if number[z] < number[x]:
    #                 if max_val < number[x]:
    #                     max_val = number[x]
    #                     max_idx = x
    #                     change_flag = True
    #         if change_flag:
    #             number[z], number[max_idx] = number[max_idx], number[z]
    #             cnt -= 1
    # for a in range(N,len(number)):
    #     if cnt > 0:
    #         change_flag = False
    #         max_val = 0
    #         max_idx = 0
    #         for x in range(len(number)-1,a,-1):
    #             if number[a] < number[x]:
    #                 if max_val < number[x]:
    #                     max_val = number[x]
    #                     max_idx = x
    #                     change_flag = True
    #         if change_flag:
    #             number[a], number[max_idx] = number[max_idx], number[a]
    #             cnt -= 1
    # number = "".join(map(str,number))
    # print(f"#{i+1} {number}")