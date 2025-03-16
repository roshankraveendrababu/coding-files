def implement_atoi(s):
    s=s.strip()
    if not s:
        return "0"
    sign=1
    i=0
    num=0
    if s[0]=="-":
        sign=-1
    elif s[0]=="+":
        sign=1
    i+=1
    while i<len(s) and s[i].isdigit():
        num=num*10+int(s[i])
        i+=1
        if num>=(2**31)-1:
            return (2**31)-1
        elif num<(-2**31):
            return (-2**31)
    return sign*num

if __name__=="__main__":
    s=input("enter the integer value : ")
    print(implement_atoi(s))