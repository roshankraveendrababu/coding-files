def longest_common_subsequence(x,y,x_ind,y_ind):
    if x_ind<0 or y_ind<0:
        return 0
    if x[x_ind]==y[y_ind]:
        return 1+longest_common_subsequence(x,y,x_ind-1,y_ind-1)
    else:
        return max(longest_common_subsequence(x,y,x_ind-1,y_ind),longest_common_subsequence(x,y,x_ind,y_ind-1))

def memo_lcs(x,y):
    t=[[-1 for _ in range(len(y))] for _ in range(len(x))]
    def lcs(x,y,x_ind,y_ind):
        if t[x_ind][y_ind]!=-1:
            return t[x_ind][y_ind]
        if x_ind<0 or y_ind<0:
            return 0
        if x[x_ind]==y[y_ind]:
            t[x_ind][y_ind]=1+lcs(x,y,x_ind-1,y_ind-1)
            return t[x_ind][y_ind]
        else:
            t[x_ind][y_ind]=max(lcs(x,y,x_ind-1,y_ind),lcs(x,y,x_ind,y_ind-1))
            return t[x_ind][y_ind]
    return lcs(x,y,len(x)-1,len(y)-1)
'''
in tabulation , always the table is constructed for 1 above the max permissible value for 0-based indexing
the inner for loops will run from 1 to 1+max permissible value
the value in arr is checked for arr[i-1] or arr[j-1].i.e, one below the curr index

'''
def tabu_lcs(x,y):
    t=[[0 for _ in range(len(y)+1)] for _ in range(len(x)+1)]
    for i in range(1,len(x)+1):
        for j in range(1,len(y)+1):
            if x[i-1]==y[j-1]:
                t[i][j]=1+t[i-1][j-1]
            else:
                t[i][j]=max(t[i-1][j],t[i][j-1])
    return t[len(x)][len(y)]

print(tabu_lcs("abced","ace"))