# 17

def solve(pw):
    stk = [pw[0]]
    for c in range(1,N):
        if stk and stk[-1] == pw[c]:
            stk.pop()
        else:
            stk.append(pw[c])
            
    return ''.join(stk)
        
for tc in range(10):
    tmp = input().split()
    N = int(tmp[0])
    pw = list(tmp[1])

    print(f'#{tc+1} {solve(pw)}')