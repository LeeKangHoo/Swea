#44

def solve(val):
    pal = val
    cnt = 0

    for i in pal[:]:
        if i != i[::-1]:
            if i[::-1] in pal:
                cnt += len(i) * 2
                pal.remove(i)
                pal.remove(i[::-1])
        else:
            if pal.count(i) >= 2:
                cnt += len(i) * 2
                pal.remove(i)
                pal.remove(i)
    max_val = 0
    for i in pal:
        if i == i[::-1]:
            max_val = max(max_val, len(i))
    
    return cnt + max_val

    



T = int(input())

for i in range(T):
    N, M = map(int,input().split())
    val = []
    for j in range(N):
        val.append(input())
    print(f"#{i+1} {solve(val)}")