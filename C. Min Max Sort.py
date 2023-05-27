t = int(input())
for i in range(t):
    n = int(input())
    li = list(map(int,input().split()))[:n]
    c = 0
    d = 0
    for i in range(n-1):
        # for j in range(i+1,n):
        #     if li[i] > li[j]:
        #         li[j],li[i] = li[i],li[j]
        #         c = c + 1
        #     else:
        #         d = d + 1
        if li[i] > li[i+1]:
            c = c + 1
    print(c)

