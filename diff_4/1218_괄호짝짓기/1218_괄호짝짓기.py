# 20
# stack을 이용해서 풀면 될 것 같네 또 너무 쉬워보이는데
# 그냥 stack을 이용해서 쌍을 맞추는 문제.

for tc in range(10):
    N = int(input())
    mapp = list(input())
    opn = ['{','[','(','<']
    close = ['}',']',')','>']
    stk = []
    flag = True
    for i in range(N):
        if stk:
            if mapp[i] in close:
                o_idx = opn.index(stk[-1])
                if mapp[i] == close[o_idx]:
                    stk.pop()
                    continue
                else:
                    flag = False
                    break
            else:
                stk.append(mapp[i])
        else:
            if mapp[i] in close:
                flag = False
                break
            stk.append(mapp[i])
    
    if flag:
        if len(stk) == 0:
            print(f'#{tc+1} 1')
        else:
            print(f'#{tc+1} 0')
    else:
        print(f'#{tc+1} 0')

