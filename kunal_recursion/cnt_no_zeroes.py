def count_num_of_zeroes(num,cnt):
    if not num:
        return cnt
    if num%10==0:
        cnt+=1
    return count_num_of_zeroes(num//10,cnt)

print(count_num_of_zeroes(400300400,0))