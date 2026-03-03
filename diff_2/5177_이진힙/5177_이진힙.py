#60 up
T = int(input())

for i in range(T):
    N = int(input())
    graph = [0]
    numbers = list(map(int,input().split()))

    for num in numbers:
        graph.append(num)
        child = len(graph) - 1
        parent = child // 2

        while parent >= 1 and graph[parent] > graph[child]:
            graph[parent], graph[child] = graph[child], graph[parent]

            child = parent
            parent = child // 2
   
    r = 0
    number = N
    while number > 1:
        number = number // 2
        r += graph[number]

            
        

    print(f"#{i+1} {r}")