#25

def solve():
    f = [False] * 4
    f[0] = True if n.find('N') != -1 else False
    f[1] = True if n.find('W') != -1 else False
    f[2] = True if n.find('S') != -1 else False
    f[3] = True if n.find('E') != -1 else False

    if f[0] != f[2]:
        return 'No'
    if f[1] != f[3]:
        return 'No'
    return 'Yes'
        

        
            

T = int(input())
for tc in range(T):
    n = input()

    print(solve())