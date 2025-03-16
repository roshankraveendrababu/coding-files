def add_basek(num1,num2,k):
    dec1=int(num1,k)
    dec2=int(num2,k)
    total=dec1+dec2
    res=""
    while total:
        remainder=total%k
        if remainder<=9:
            res=chr(48+remainder)+res
        else:
            res=chr(remainder+65)+res
        total//=k
    return res 

if __name__=="__main__":
    k=int(input("enter the base of the numbers: "))
    num1=input(f"enter the number1 in base {k}: ")
    num2=input(f"enter the number 2 in base {k}: ")
    print(add_basek(num1,num2,k))