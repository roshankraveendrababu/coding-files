def helper(word):
    if word=="":
        return ""
    cur_word=word[0] if word[0]!="a" else ""
    next_iter=helper(word[1:]) 
    return cur_word+next_iter

def with_args(word,cur_word):
    if word=="":
        return cur_word
    if word[0]!="a":
        cur_word+=word[0]
    return with_args(word[1:],cur_word)

def remove_a(word):
    return helper(word)

print(remove_a("raveendra babu"))