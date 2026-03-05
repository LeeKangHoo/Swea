#16
import math
T = int(input())

for i in range(T):
    S, P = map(int,input().split())
    
    D = S**2 - 4*P
    if D >= 0:
        root_D = int(math.sqrt(D))
        if root_D**2 == D:
            print("Yes")
        else:
            print("No")
    else:
        print("No")