#10
# 1 >> 0, 4, 6, 9
# 2 >> 8
T = int(input())


for i in range(T):
    N = int(input())
    
    if N == 1:
        print(0)
        continue

    if N % 2 == 1:
        print("4",end='')
    
    for a in range(N//2):
        print("8",end='')
    
    print("")
    
