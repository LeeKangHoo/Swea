#20
T = int(input())

for i in range(T):
    n = int(input())
    num = input()
    num = sorted(num, reverse=True)
    v1 = max(set(num), key=num.count)
    print(f"#{i+1} {v1} {num.count(v1)}")