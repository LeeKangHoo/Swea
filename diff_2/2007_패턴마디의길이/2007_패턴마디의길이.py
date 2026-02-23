#10
T = int(input())

for i in range(T):
    s = input().strip()

    for j in range(1,11):
        if s[:j] == s[j:j*2]:
            answer = j
            break

    print(f"#{i+1} {answer}")