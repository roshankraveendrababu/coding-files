def longest_palindromic_subseq(str1):
    str2=str1[::-1]
    return lcs(str1,str2)

def lcs(str1,str2):
    t=[[0 for _ in range(len(str2)+1)] for _ in range(len(str1)+1)]
    for i in range(1,len(str1)+1):
        for j in range(1,len(str2)+1):
            if str1[i-1]==str2[j-1]:
                t[i][j]=1+t[i-1][j-1]
            else:
                if t[i-1][j]>t[i][j-1]:
                    t[i][j]=t[i-1][j]
                else:
                    t[i][j]=t[i][j-1]
    n,m=len(str1),len(str2)
    lps_arr=[]
    while n>0 and m>0:
        if str1[n-1]==str2[m-1]:
            lps_arr.append(str1[n-1])
            n-=1
            m-=1
        else:
            if t[n-1][m]>t[n][m-1]:
                n-=1
            else:
                m-=1
    return "".join(reversed(lps_arr))

print(longest_palindromic_subseq("cbbd"))
