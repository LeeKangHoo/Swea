#2
T = int(input())

for i in range(T):
    v1 = input()
    if v1 == v1[::-1]:
        print(f"#{i+1} 1")
    else:
        print(f"#{i+1} 0")