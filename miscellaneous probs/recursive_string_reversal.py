"""
def reverse(str_word):
    n=len(str_word)
    if n==1:
        return str_word
    return str_word[n-1]+reverse(str_word[:n-1])
"""


def recursive_decimal_to_binary(num):
    if num<2:
        return (num%2)
    return num%2+recursive_decimal_to_binary(num//2)*10

#print(recursive_decimal_to_binary(14))
#print(reverse("srilekha"))