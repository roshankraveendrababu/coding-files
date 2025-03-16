def findN_baseK(num,k,n):
    res=""
    while num:
        remainder=num%k
        if remainder<=9:
            res=chr(48+remainder)+res
        else:
            res=chr(65+remainder)+res
        num//=k
    return res[n-1]

print(findN_baseK(10,2,2))
