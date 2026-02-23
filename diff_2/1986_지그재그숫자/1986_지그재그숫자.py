import math
#11
T = int(input())

for i in range(T):
    n = int(input())
    v1 = 0
    for a in range(1,n+1):
        if a % 2 == 0:
            v1 += a*(-1)
        else:
            v1 += a
    
    print(f"#{i+1} {v1}")