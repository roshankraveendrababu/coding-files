def fun(n):
    if n==0:
        return 
    fun(n-1)
    print(n)
if __name__=="__main__":
    fun(5)