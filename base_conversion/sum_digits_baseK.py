def sum_digits_baseK(num,N):
    res=""
    while num:
        remainder=num%N
        if remainder<=9:
            res=chr(remainder+48)+res
        else:
            res=chr(65+remainder)+res
        num//=N
    sod=0
    for i in range(len(res)-1,-1,-1):
        if res[i].isdigit():
            sod+=int(res[i])
        else:
            sod+=((ord(res[i])-ord('A'))+10)
    return sod

if __name__=="__main__":
    num=int(input("enter an number in base 10: "))
    N=int(input("enter the base to convert to: "))
    print(sum_digits_baseK(num,N))
