#14
T = int(input())

for i in range(T):
    N, num = input().split()
    N = int(N)
    result = ""
    for j in range(N):
        result += format(int(num[j], 16), '04b')
    print(f"#{i+1} {result}")

