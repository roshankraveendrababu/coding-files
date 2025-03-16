prime=101
def pattern_matching(text,pattern):
    n=len(text)
    m=len(pattern)
    text_hash=create_hash(text,m-1)
    pattern_hash=create_hash(pattern,m-1)
    result=[]
    for i in range(n-m+1):
        if pattern_hash==text_hash:
            if check_equal(text[i:i+m],pattern):
                result.append(i)
        if i<n-m:
            text_hash=recalculate_hash(text, i, i+m, text_hash, m)
    return result

def create_hash(text,n):
    hash_cnt=0
    for i in range(n+1):
        hash_cnt+=ord(text[i])*pow(prime,i)
    return hash_cnt

def check_equal(str1,str2):
    if len(str1)!=len(str2):
        return False
    for st1,st2 in zip(str1,str2):
        if st1!=st2:
            return False
    return True

def recalculate_hash(text,start,end,old_hash,pat_len):
    new_hash=old_hash-ord(text[start])
    new_hash//=prime
    new_hash+=ord(text[end])*(prime**(pat_len-1))
    return new_hash    

print(pattern_matching("Roshankonidhala", "a"))