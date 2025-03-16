def skip_word(sentence,word):
    if sentence=="":
        return ""
    if sentence[:len(word)]==word:
        return ""+skip_word(sentence[len(word):],word)
    else:
        return sentence[0]+skip_word(sentence[1:],word)
    
print(skip_word("raveendra babu ravindra jadeja","rav"))
    