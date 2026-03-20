#9
def solve(num):
    cur = ['0'] * len(num)
    cnt = 0
    while cur != num:
        for i in range(len(num)):
            if cur[i] != num[i]:
                v1 = num[i]
                for j in range(i,len(cur)):
                    cur[j] = v1
                cnt += 1
    return cnt

T = int(input())

for tc in range(T):
    num = list(input())
    
    print(f"#{tc+1} {solve(num)}")