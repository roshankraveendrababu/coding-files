def check_palindrome(num,K):
    res=""
    while num:
        remainder=num%K
        if remainder<=9:
            res=chr(remainder+48)+res
        else:
            res=chr(remainder+65)+res
        num//=K
    n=len(res)
    r=n-1
    l=0
    while l<r:
        if res[l]==res[r]:
            l+=1
            r-=1
        else:
            return False
    return True

if __name__=="__main__":
    num=int(input("enter the decimal number: "))
    K=int(input("enter the base to convert to: "))
    print(check_palindrome(num,K))