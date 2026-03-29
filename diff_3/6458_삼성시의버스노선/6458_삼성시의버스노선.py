#21
T = int(input())

for i in range(T):
    N = int(input())
    line = []
    C = []
    
    for j in range(N):
        v1, v2 = map(int,input().split())
        line.append((v1,v2))
    P = int(input())
    for z in range(P):
        tmp = int(input())
        C.append(tmp)
    r = [0] * 5001
    
    for a1,a2 in line:
        for x in range(a1,a2+1):
            r[x] += 1
    result = []
    for y in C:
        result.append(r[y])
    print(f"#{i+1}",*result)
