def convert_base_6(num):
    number=0
    copy=num
    power=1
    while(copy):
        remainder=copy%6
        number=remainder*power+number
        copy//=6
        power*=10
    return number

def find_sequence(N,arr):
    sum_digit_base6=[]
    for num in arr:
        base_6_number=(convert_base_6(num))
        
        sod=0
        while(base_6_number):
            sod+=(base_6_number%10)
            base_6_number//=10
        sum_digit_base6.append(sod)
    cnt=0
    for i in range(N):
        for j in range(i+1,N):
            if sum_digit_base6[j]<sum_digit_base6[i]:
                cnt+=1
    return cnt

if __name__=="__main__":
    N=int(input("enter the no of elements: "))
    arr=input("enter the values as comma seperated integers: ")
    arr=list(map(int,arr.split(",")))
    print(find_sequence(N,arr))