#15
def check(v1):
    cur = str(v1)
    for i in range(len(cur)-1):
        if cur[i] > cur[i+1]:
            return False
        
    return True


T = int(input())

for i in range(T):
    N = int(input())
    max_val = 0
    l = list(map(int,input().split()))

    for j in range(N):
        for z in range(N):
            tmp = l[j] * l[z]
            if z == j or len(str(tmp)) == 1:
                continue 
            if check(tmp):
                max_val = max(max_val,tmp)
    if max_val == 0:
        print(f"#{i+1} {-1}")
    else:
        print(f"#{i+1} {max_val}")