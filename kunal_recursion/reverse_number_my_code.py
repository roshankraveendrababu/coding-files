def reverse_number(num,power):
    if num<10:
        return num
    return num%10*(10**power)+reverse_number(num//10,power-1)

if __name__=="__main__":
    num=int(input())
    copy=num
    no_of_power=0
    while copy:
        no_of_power+=1
        copy//=10
    print(reverse_number(num,no_of_power-1))