#2
T = int(input())

for i in range(T):
    n = int(input())
    num = list(map(int, input().split()))
    print(f"#{i+1} {max(num) - min(num)}")
