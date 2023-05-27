t = int(input())
for i in range(t):
    n = int(input())
    s = input()[:n]
    if n == 1:
        print(1)
    elif n % 2 == 0:
        li = []
        li1 = []
        mid = n // 2
        for i in range(n-1,mid-1,-1):
            li1.append(s[i])

        for i in range(mid):
            li.append(s[i])
        c = 0
        for i in range(len(li)):
            if li[i] == li1[i]:
                c = i+1
                break
        if c == len(li):
            print(2)
        elif c == 0:
            print(0)
        else:
            r = (len(li) - c)+1
            print(2*r)
    else:
        li = []
        li1 = []
        mid = n // 2
        for i in range(n - 1, mid - 1, -1):
            li1.append(s[i])

        for i in range(mid):
            li.append(s[i])
        c = 0
        for i in range(len(li)):
            if li[i] == li1[i]:
                c = i + 1
                break
        if c == len(li):
            print(3)
        elif c == 0:
            print(1)
        else:
            r = (len(li) - c) + 1
            print((2 * r)+1)

