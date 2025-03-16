import random
def no_dup_element_substring(str_with_dup):
    freq_array=[0]*256
    freq_array[ord(str_with_dup[0])]+=1
    l=0
    r=1
    longest_substr=float('-inf')
    n=len(str_with_dup)
    while r<n:
        if freq_array[ord(str_with_dup[r])]:
            while freq_array[ord(str_with_dup[r])] and l<r:
                freq_array[ord(str_with_dup[l])]-=1
                l+=1
        else:
            freq_array[ord(str_with_dup[r])]=1
            longest_substr=max(longest_substr,r-l+1)
        r+=1
    return longest_substr

if __name__=="__main__":
    str_with_dup=""
    for i in range(20):
        str_with_dup+=chr(random.randint(97,105))
    print(str_with_dup)
    print(no_dup_element_substring(str_with_dup))

