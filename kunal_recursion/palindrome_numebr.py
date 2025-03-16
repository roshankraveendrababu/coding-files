def is_palindrome(num,power):
    if num<10:
        return True
    if (num//(10**power))!=num%10:
        return False
    return is_palindrome((num%10**power)//10,power-2)

print(is_palindrome(11,1))
