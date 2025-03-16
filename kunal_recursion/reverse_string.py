def reverse_string(word,low,high):
    if low>=high:
        return
    word[low],word[high]=word[high],word[low]
    return reverse_string(word,low+1,high-1)

if __name__=="__main__":
    word=input()
    word_list=list(word)
    reverse_string(word_list,0,len(word)-1)
    word="".join(word_list)
    print(word)
    