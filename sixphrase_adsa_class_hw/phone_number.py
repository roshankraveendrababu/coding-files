def number_to_words(number):
    # Map of digits to their word forms
    num_words = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    copy=number
    
    # Initialize variables
    result = ""  # We will accumulate the result here
    #temp=copy%10
    cnt=0
    while copy:
        digit1=copy%10
        digit2=(copy%100)//10
        digit3=(copy%1000)//100
        digit4=(copy%10000)//1000
        #digit5=(copy%100000)//10000
        #digit6=(copy%1000000)//100000
        #digit7=(copy%10000000)//1000000
        #digit8=(copy%100000000)//10000000
        #digit9=(copy%1000000000)//100000000
        #digit10=(copy%100000000)//10000000000
        if digit1==digit2 and digit2!=digit3 and digit2!=0:
            result="Double"+" "+num_words[digit1]+" "+result
        elif digit1==digit2 and digit2==digit3 and digit3!=0:
            result="Triple"+" "+num_words[digit1]+" "+result
        elif digit1==digit2==digit3==digit4 and digit4!=0:
            result="Double"+" "+num_words[digit1]+" "+ "Double"+" "+num_words[digit1]+" "+result
        elif digit1!=0:
            result=num_words[digit1]+" "+result
        else:
            break
        #temp=digit1
        copy//=10
    return result
            


# Test cases
print(number_to_words(9442161065))  # Expected: "Nine Double Four Two One Six One Zero Six Five"
print(number_to_words(9994466665))  # Expected: "Triple Nine Double Four Double Six Double Six Five"
print(number_to_words(9999999999))  # Expected: "Triple Nine Triple Nine Double Nine Double Nine"
