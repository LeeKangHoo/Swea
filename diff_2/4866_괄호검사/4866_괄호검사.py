#
T = int(input())

for i in range(T):
    v1 = input()
    v2 = []
    for x in v1:
        if '{' == x:
            v2.append(x)
        elif '}' == x:
            v2.append(x)
        if '(' == x:
            v2.append(x)
        elif ')' == x:
            v2.append(x)
            
    if len(v2)%2 == 1:
        print(f"#{i+1} 0")
        continue

    while True:
        found = False
        for y in range(len(v2)-1):
            if (v2[y] == '(' and v2[y+1] == ')') or (v2[y] == '{' and v2[y+1] == '}'):
                del v2[y+1]
                del v2[y]
                found = True
                break
        
        if not found:
            break
            

                    
    if len(v2) == 0:
        print(f"#{i+1} 1")
    else:
        print(f"#{i+1} 0")


            