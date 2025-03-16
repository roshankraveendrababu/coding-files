def integeer_roman(number):
    symlist = [
        ("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
        ("C", 100), ("XC", 90), ("L", 50), ("XL", 40),
        ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)
    ]
    res=""
    for sys,val in (symlist):
        if number//val:
            cnt=number//val
            res+=sys*cnt
            number%=val
    return res

if __name__=="__main__":
    number=int(input("enter the number that has to be converted to roman: "))
    print(integeer_roman(number))