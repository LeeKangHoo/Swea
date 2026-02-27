#4
T = int(input())

for i in range(T):
    v1 = input()
    v2 = input()
    max_val = 0
    for x in v1:
         max_val = max(max_val,v2.count(x))
    print(f"#{i+1} {max_val}")