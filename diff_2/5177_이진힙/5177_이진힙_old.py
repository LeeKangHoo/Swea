#
T = int(input())

for i in range(T):
    N = int(input())
    graph = [0] + list(map(int,input().split()))
    check = False
    while not check:
        for a in range(1,N+1):
                    if a * 2 > N:
                        break
                    if graph[a*2] < graph[a]:
                        graph[a*2], graph[a] = graph[a], graph[a*2]
                    if a * 2 + 1 > N:
                        break
                    if graph[a*2+1] < graph[a]:
                        graph[a*2+1], graph[a] = graph[a], graph[a*2+1]

        for x in range(1,N+1):
            if x * 2 + 1 > N:
                break
            if graph[x*2] < graph[x] or graph[x*2+1] < graph[x]:
                continue
        check = True
    r = 0
    number = N
    while number > 1:
        if N % 2 == 0:
            number = number//2
        
        if N % 2 == 1:
            number = (number - 1)//2
            
        r += graph[number]

    print(f"#{i+1} {r}")

                
        
        
        
                
