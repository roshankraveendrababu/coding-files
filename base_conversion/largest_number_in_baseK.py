def rearrange_maxDigit(num,K):
    n=len(num)
    num=str(num)
    num_list=list(num)
    for i in range(n):
        j=i
        while j>0 and ord(str(num_list[j-1]))>ord(str(num_list[j])):
            num_list[j-1],num_list[j]=num_list[j],num_list[j-1]
            j-=1
    return ''.join(num_list[::-1])

print(rearrange_maxDigit("ABC123",16))