'''
given two strings a and b , return the shortest common super sequence that contains both the string the same order.
as per intuition, we should not have redundant character and the redundant characters are lcs of these two strings
hence we find the lcs and construct the supersequence with its tabulated form


'''
def shortest_supersequence(x,y):
    t=[[0 for _ in range(len(y)+1)] for _ in range(len(x)+1)]
    for i in range(1,len(x)+1):
        for j in range(1,len(y)+1):
            if x[i-1]==y[j-1]:
                t[i][j]=1+t[i-1][j-1]
            else:
                if t[i-1][j]>t[i][j-1]:
                    t[i][j]=t[i-1][j]
                else:
                    t[i][j]=t[i][j-1]

    n,m=len(x),len(y)
    super_sect=[]
    while n>0 and m>0:
        if x[n-1]==y[m-1]:
            super_sect.append(x[n-1])
            n-=1
            m-=1
        else:
            if t[n-1][m]>t[n][m-1]: # the value at left is greater than the top element
                super_sect.append(x[n-1])
                n-=1
            else:
                super_sect.append(y[m-1])
                m-=1
    # add remaining elements 
    while n>0:
        super.sect.append(x[n-1])
        n-=1
    while m>0:
        super_sect.append(y[m-1])
        m-=1
    return "".join(reversed(super_sect))

print(shortest_supersequence("abac","cab"))