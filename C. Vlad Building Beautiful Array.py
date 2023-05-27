t = int(input())
for i in range(t):
    n = int(input())
    li = list(map(int,input().split()))[:n]
    odd = []
    even = []
    for i in range(n):
        if li[i] % 2 == 0:
            even.append(li[i])
        else:
            odd.append(li[i])

    odd.sort()
    even.sort()
    a_even = True
    b_odd = True
    #even check
    for i in range(n):
        if li[i] % 2 == 0:
            continue
        elif not odd or odd[0] >= li[i]:
            a_even = False
            break
    #odd check
    for i in range(n):
        if li[i] % 2 != 0:
            continue
        elif not odd or odd[0] >= li[i]:
            b_odd = False
            break

    if b_odd or a_even:
        print("YES")
    else:
        print("NO")



