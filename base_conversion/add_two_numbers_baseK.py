def add_basek(num1,num2,k):
    m=len(num1)
    n=len(num2)
    num1=num1[::-1]
    num2=num2[::-1]
    carry=0
    res=""
    for i in range((max(m,n))):
        digit1=int(num1[i]) if i<len(num1) else 0
        digit2=int(num2[i]) if i<len(num2) else 0
        total=digit1+digit2+carry
        res=str(total%k)+res
        carry=total//k
    if carry:
        return "1"+res
    return res

if __name__=="__main__":
    k=int(input("enter the base of the numbers: "))
    num1=input("enter the first number: ")
    num2=input("enter the second number: ")
    print(add_basek(num1,num2,k))

