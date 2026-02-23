#
T = int(input())

for i in range(T):
    n = int(input())
    print(f"#{i+1}")

    row = [1]

    for j in range(n):
        print(*(row))
        next_row = [1]

        for k in range(len(row) - 1):
            next_row.append(row[k] + row[k+1])

        next_row.append(1)
        row = next_row
        