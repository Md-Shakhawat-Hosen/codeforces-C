t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    li = list(s)
    li1 = list(set(li))
    if len(li) == len(li1):
        print("YES")
    else:
        flag = 0
        ll = []
        l3 = []
        for i in range(len(li1)):
            r = li.count(li1[i])
            if r >= 2:
                ll.append(li1[i])
            else:
                l3.append(li1[i])

        for i in range(len(ll)):
            v = ll[i]
            if i % 2 == 0:
                s = s.replace(v,'0')
            else:
                s = s.replace(v,'1')

        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                flag = 1
                break


        if flag == 1:
            print("NO")
        else:
            for i in range(len(l3)):
                ind = s.index(l3[i])
                if ind == 0:
                    if s[ind+1] == '0':
                        s.replace(s[ind],'1')
                    else:
                        s.replace(s[ind], '0')
                elif ind == len(s)-1:
                    if s[ind-1] == '0':
                        s.replace(s[ind],'1')
                    else:
                        s.replace(s[ind], '0')
                elif s[ind+1] == '1' and s[ind-1] == '1':
                    if s[ind+1] == '1' and s[ind-1] == '1':
                        s.replace(s[ind],'0')
                    else:
                        s.replace(s[ind], '1')

                elif (s[ind+1] != '0' or s[ind-1] != '0') or (s[ind+1] != '1' or s[ind-1] != '1'):


            for i in range(len(s)):



