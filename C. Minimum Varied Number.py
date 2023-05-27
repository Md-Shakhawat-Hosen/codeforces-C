t = int(input())
for i in range(t):
    s = int(input())
    li = []
    x = 9
    while s:
        if x >= s:
            li.append(s)
            break
        else:
            li.append(x)
            s = s - x
            x = x - 1
    li.reverse()
    for item in li:
        print(item,end="")
    print()
