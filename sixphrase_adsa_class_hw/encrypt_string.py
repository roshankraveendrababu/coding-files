def encrypt_string(string_no_frequency):
    freq_arr=[0]*256
    n=len(string_no_frequency)
    for i in range(n):
        freq_arr[ord(string_no_frequency[i])]+=1
    encrypted_string=""
    for i in range(97,123):
        if freq_arr[i]>0:
            encrypted_string+=chr(i)
            encrypted_string+=str(freq_arr[i])
    return encrypted_string

print(encrypt_string("sfkjhfslkjhdfgkjlsdhfkjfdhkjsfdyiqtyerituyriutweryi"))