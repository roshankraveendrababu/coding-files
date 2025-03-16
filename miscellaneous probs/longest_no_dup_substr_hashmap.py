import random
def longest_substr_with_no_repeating_chars(str_with_dup):
    freq_map={}
    l=0
    r=0
    n=len(str_with_dup)
    longest_substr=float('-inf')
    #freq_map.get(str_with_dup[l],0)+=1
    while r<n:
        while freq_map.get(str_with_dup[r],0)>0:
            freq_map[str_with_dup[l]]-=1
            l+=1
        freq_map[str_with_dup[r]]=freq_map.get(str_with_dup[r],0)+1
        longest_substr=max(longest_substr,r-l+1)
        r+=1
    return longest_substr

if __name__=="__main__":
    str_with_dup=""
    for i in range(20):
        str_with_dup+=chr(random.randint(97,105))
    print(str_with_dup)
    print(longest_substr_with_no_repeating_chars(str_with_dup))