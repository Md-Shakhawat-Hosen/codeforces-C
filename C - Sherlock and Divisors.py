T = int(input())
for x in range(T):
    n = int(input())
    li = []
    count = 0
    for i in range(2,int(n/2)+1):
        if n % i == 0:
            li.append(i)

    li.append(n)
    for x in li:
        if x % 2 == 0:
            count = count + 1

    print(count)