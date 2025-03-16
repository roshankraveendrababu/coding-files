def xor_on_baseN(num1,num2,N):
    int_num1=int(num1,N)
    int_num2=int(num2,N)
    bin_str_num1=""
    while int_num1:
        remainder=int_num1%2
        bin_str_num1=str(remainder)+bin_str_num1
        int_num1//=2
    
    bin_str_num2=""
    while int_num2:
        remainder=int_num2%2
        bin_str_num2=str(remainder)+bin_str_num2
        int_num2//=2

    len_str_num1=len(bin_str_num1)
    len_str_num2=len(bin_str_num2)
    i=0
    j=0
    final_str_bin=""
    while i<len_str_num1 or j<len_str_num2:
        first_ele=int(bin_str_num1[i]) if i<len_str_num1 else 0
        second_ele=int(bin_str_num2[j]) if j<len_str_num2 else 0
        final_str_bin=str(first_ele^second_ele)+final_str_bin
        i+=1
        j+=1

    int_ans=int(final_str_bin,2)
    final_str_N=""
    while int_ans:
        remainder=int_ans%N
        final_str_N=str(remainder)+final_str_N
        int_ans//=N

    return final_str_N

print(xor_on_baseN("3","5",10))    