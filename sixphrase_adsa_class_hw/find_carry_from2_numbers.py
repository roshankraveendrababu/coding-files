class carry_addition:
    def find_carry(self,num1,num2):
        copy_num1=num1
        copy_num2=num2
        if copy_num1>copy_num2:
            copy_num1,copy_num2=copy_num2,copy_num1
        #print(copy_num1)
        sum_of_carry=0
        carry=0
        while(copy_num2):
            dig1=copy_num1%10
            dig2=copy_num2%10
            if carry+dig1+dig2>9:
                carry=1
                sum_of_carry+=1
            else:
                carry=0
            copy_num1//=10
            copy_num2//=10
        return sum_of_carry

if __name__=="__main__":
    number_addition=carry_addition()
    num1=int(input("enter the first number: "))
    num2=int(input("enter the second number: "))
    print(number_addition.find_carry(num1,num2))

    
    