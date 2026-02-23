#7
T = int(input())

for i in range(T):
    N,M = map(int, input().split())
    num = list(map(int,input().split()))
    r = []
    
    for j in range(N-M+1):
        r.append(sum(num[j:j+M]))
    print(f"#{i+1} {max(r) - min(r)}")