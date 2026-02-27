#47

def judge(index1,index2,mapp):
    A = mapp[index1]
    B = mapp[index2]
    if (A - B) == 0:
        return index1
    elif (A - B) == -1:
        return index2
    elif (A - B) == 1:
        return index1
    elif (A - B) == -2:
        return index1
    elif (A - B) == 2:
        return index2


def solve(mapp,i,j):
    
    if i == j:
        return i
    
    first = solve(mapp,i,(i+j)//2)
    second = solve(mapp,(i+j)//2+1,j)

    return judge(first,second,mapp)
    

T = int(input())

for i in range(T):
    N = int(input())
    mapp = list(map(int,input().split()))

    print(f"#{i+1} {solve(mapp,0,N-1)+1}")