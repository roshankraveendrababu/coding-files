def print_row(row_num):
    ans=[1]
    for i in range(1,row_num+1):
        ans.append(factorial(row_num-1,i-1))
    
    print(ans)

def factorial(n,k):
    ans=1
    for i in range(k):
        ans*=(n-i)
        ans//=(i+1)
    return ans

print_row(6)
