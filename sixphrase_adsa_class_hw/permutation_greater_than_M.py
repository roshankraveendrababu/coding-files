def smallest_number_greater_than_m(N, M):
    digit=sorted(str(N))
    while True:
        num=int(''.join(digit))
        if (num)>M:
            return num
        if not next_permutation(digit):
            return "Not Possible"
def next_permutation(digit):
    n=len(digit)
    pivot=-1
    i=n-2
    while i>=0 and digit[i]>digit[i+1]:
        i-=1
    pivot=i
    if pivot==-1:
        return False
    j=n-1
    while digit[j]<digit[i]:
        j-=1
    digit[pivot],digit[j]=digit[j],digit[pivot]
    digit[pivot+1:]=sorted(digit[pivot+1:])
    return True




# Examples
print(smallest_number_greater_than_m(218765, 265000))  # Output: 265178
#print(smallest_number_greater_than_m("218765", "290000"))  # Output: 512678
#print(smallest_number_greater_than_m("218765", "900000"))  # Output: 265178


#print(smallest_number_greater_than_m("218765","265000"))

