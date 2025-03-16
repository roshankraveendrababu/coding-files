def lps(pat):
    lps_arr=[0]*len(pat)
    index=0
    i=1
    while i<len(pat):
        if pat[i]==pat[index]:
            lps_arr[i]=index+1
            index+=1
            i+=1
        else:
            if index!=0:
                index=lps_arr[index-1]
            else:
                lps_arr[i]=0
                i+=1
    return lps_arr

def find_index(txt,pat):
    res=[]
    m=len(txt)
    n=len(pat)
    i=0
    j=0
    lps_arr=lps(pat)
    while i<m and j<n:
        if txt[i]==pat[j]:
            i+=1
            j+=1
            if j==n-1:
                res.append(i-j)
                j=lps_arr[j-1]
        else:
            if j!=0:
                j=lps_arr[j-1]
            else:
                i+=1
    return res

print(find_index("abxabcabcaby","abcaby"))



