class SixphraseHW:
    def  is_nobita(self,num):
        copy=num
        while(copy>9):
            num1=copy%10
            num2=(copy%100)//10
            if abs(num2-num1)==1:
                copy//=10
            else:
                return False
        return True

    def sum_nobita_numbers(self,start,end):
        sum=0
        for num in range(start,end+1):
            if self.is_nobita(num):
                sum+=num
        return sum
    
if __name__=="__main__":
        hw_instance=SixphraseHW()
        string_input=input("enter the starting and ending value seperated by a single space: ")
        i=0
        n=len(string_input)
        for i in range(n):
            if string_input[i]==" ":
                break
        start=int(string_input[0:i])
        end=int(string_input[i+1:])
        print(hw_instance.sum_nobita_numbers(start,end))

            
    
