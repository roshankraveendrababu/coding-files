def multiply_baseK(num1,num2,K):
    dec_num1=int(num1,K)
    dec_num2=int(num2,K)
    multiple=dec_num1*dec_num2
    res=""
    while multiple:
        remainder=multiple%K
        if remainder<=9:
            res=chr(remainder+48)+res
        else:
            res=chr(65+remainder)+res
        multiple//=K
    return res or "0"

if __name__=="__main__":
    K=int(input("enter the base of the numbers: "))
    num1=input(f"enter the first number in base {K}: ")
    num2=input(f"enter the number 2 in base {K}: ")
    print(multiply_baseK(num1,num2,K))