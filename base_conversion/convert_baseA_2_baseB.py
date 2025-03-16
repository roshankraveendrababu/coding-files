def convert_bases(num,A,B):
    dec_num=int(num,A)
    res=""
    while dec_num:
        remainder=dec_num%B
        if remainder<=9:
            res=chr(remainder+48)+res
        else:
            res=chr(remainder+65)+res
        dec_num//=B
    return res

if __name__=="__main__":
    A=int(input("enter the base of input number: "))
    num=input("enter the number to be converted: ")
    B=int(input("enter the to-be converted base: "))
    print(convert_bases(num,A,B))
