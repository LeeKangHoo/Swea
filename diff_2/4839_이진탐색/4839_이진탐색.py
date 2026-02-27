#30
T = int(input())

def solve(P,target):
    c = 0
    r = P
    l = 1
    cnt = 0

    while c != target:
        c = int((l+r)/2)
        cnt += 1
        if (target - c) < 0:
            r = c
        else:
            l = c
    return cnt


for i in range(T):
    P,A,B = map(int,input().split())
    r = ''
    
    if solve(P,A) > solve(P,B):
        r = "B"
    elif solve(P,A) < solve(P,B):
        r = "A"
    else:
        r = "0"
    print(f"#{i+1} {r}")

    
    

    