def Nth_in_decrypted(encryped_string,ind):
    decrypt_string=""
    n=len(encryped_string)
    for i in range(0,n,2):
        decrypt_string+=encryped_string[i]*int(encryped_string[i+1])
    a=len(decrypt_string)
    return decrypt_string[ind-1] if ind-1<a else "-1"

print(Nth_in_decrypted("a5n7b9r5",23))

# this code will not pass all the test cases coz it cant handle when the count of character in the original string is 10 or above 1
