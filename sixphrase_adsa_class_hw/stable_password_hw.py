#from collections import Counter
class sixphrasethrusdayHW:
    def is_stable(self,num):
        freq_map={}
        copy=num
        temp=num%10
        while(copy):
            digit=copy%10
            freq_map[digit]=1+freq_map.get(digit,0)
            copy//=10
        first_element_count=freq_map[temp]
        for value in freq_map.values():
            if value !=first_element_count:
                return False
        return True
    
    def find_password(self,int1,int2,int3,int4,int5):
        stable_sum=0
        unstable_sum=0
        arr_inputs=[int1,int2,int3,int4,int5]
        for input in arr_inputs:
            if self.is_stable(input):
                  stable_sum+=input
            else:
                  unstable_sum+=input
        return stable_sum-unstable_sum

if __name__=="__main__":
    check_first_time=sixphrasethrusdayHW()
    int1=(int(input(f"enter the 1st value: ")))
    int2=(int(input(f"enter the 2nd value: ")))
    int3=(int(input(f"enter the 3rd value: ")))
    int4=(int(input(f"enter the 4th value: ")))
    int5=(int(input(f"enter the 5th value: ")))

    print(check_first_time.find_password(int1,int2,int3,int4,int5))





    



    