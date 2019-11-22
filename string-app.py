def cost1(s2) :
    cost = 0
    s1 = s2.replace('R','1')
    s = s1.replace('G','0')
    #print(s2,s)
    L = list(s)
    if len(s) == 2 :
        if s in ['10', '01'] :
            return 0
        elif s=='11' :
            return 5
        else :
            return 3
    elif len(s)>=3 :
        if s[:3] == '110' :
            cost = 5
            L[0] = '0'
        elif s[:3] == '111' :
            cost = 5
            L[1] = '0'
        elif s[:3] == '001' :
            cost = 3
            L[0] = '1'
        elif s[:3] == '000' :
            cost = 3
            L[1] = '1'
    #print(2,''.join(L),cost)
    if L[0]=='1' :
        c = '0'
        for i in range(1,len(L)) :
            #print(11,i,L)
            if L[i] != c :
                #print(11,i,L[i],c)
                if c=='1' :
                    cost += 3
                    L[i] = c
                    c = '0'
                else :
                    cost += 5
                    L[i] = c
                    c = '1'
            else :
                if c=='0' : c = '1'
                else :      c = '0'
    elif L[0]=='0' :
        c = '1'
        for i in range(1,len(L)) :
            #print(12,i,L,c)
            if L[i] != c :
                #print(122, i, L[i], c)
                if c=='1' :
                    cost += 3
                    L[i] = c
                    c = '0'
                else :
                    cost += 5
                    L[i] = c
                    c = '1'
            else :
                if c=='0' : c = '1'
                else :      c = '0'
    #print('res=',''.join(L))
    return cost
# Driver Code 
n,b = [int(x) for x in input().split()]
sum1 = 0
for i in range(n) :
    s = input()
    sum1 += cost1(s)
print(sum1,end='')


