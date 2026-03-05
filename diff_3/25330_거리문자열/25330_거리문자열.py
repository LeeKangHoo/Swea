#59
from collections import deque
def solve(number):
    q = deque()
    visited = []
    check = [False] * len(number)
    for i in set(number):
        if number.count(i) != 2:
            return "no"
    
    for cur in range(len(number)):
        if check[cur]:
            continue
        q.append(number[cur])
        if len(number) - 1 < cur+1+int(q[0]):
            return "no"
        if q[0] == number[cur+1+int(q[0])]:
            check[cur] = True
            check[cur+1+int(q[0])] = True
            q.popleft()
            
    
    if len(q) == 0:
        return "yes"
    else:
        return "no"


T = int(input())

for i in range(T):
    number = input()
    print(f"{solve(number)}")