symlist={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
def convert_to_integer(roman):
    ans_res=0
    n=len(roman)
    for i in range(n):
        if i<n-1:
            if symlist[roman[i]]>=symlist[roman[i+1]]:
                ans_res+=symlist[roman[i]]
            else:
                ans_res-=symlist[roman[i]]
        else:
            ans_res+=symlist[roman[i]]
    return ans_res

if __name__=="__main__":
    roman=input("enter the number in roman numerical form: ")
    print(convert_to_integer(roman))
                

