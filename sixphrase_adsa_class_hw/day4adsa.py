#word_map={1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",0:"zero"}
#num=int(input("enter the number please: "))
import random
import math
from collections import deque
import time
#power=1
#sum_of_digits=0
#res=""
#while (num//power):
    #digit=(num//power)%10
    #sum_of_digits+=digit
    #power*=10
    #res=word_map[digit]+" "+res
#print(sum_of_digits)
#print(res)
#print(num)
def msd_focus(num):
    num_str=str(num)
    for i in (num_str):
        yield word_map[int(i)]
#for digit in msd_focus(num):
    #print(digit, end=" ")
#print(num)

def maximum_subarray():
    size_array=int(input("enter the size of the array: "))
    nums=[]
    for i in range(size_array):
        nums.append(random.randint(1,100))
    for i in range(size_array):
        print(nums[i],end=" ")
    window_size=int(input("enter the size of the window: "))
    
    curr_sum=0
    for i in range(window_size):
        curr_sum+=nums[i]
    max_sum=curr_sum
    window_begin, window_end = 0, window_size - 1
    for j in range(size_array-window_size):
        curr_sum-=nums[j]
        curr_sum+= nums[j+window_size]
        if curr_sum>max_sum:
            max_sum=max(max_sum,curr_sum)
            window_begin=j
            window_end=j+window_size-1
    return max_sum,nums[window_begin],nums[window_end]

def max_in_subarray():
    size_array=int(input("enter the size of the array: "))
    nums=[]
    for i in range(size_array):
        nums.append(random.randint(1,100))
    for i in range(size_array):
        print(nums[i],end=" ")
    window_size=int(input("enter the size of the window: "))
    r=l=0
    q=deque()
    output=[]
    while r<size_array:
        while q and nums[q[-1]]<nums[r]:
            q.pop()
        q.append(r)
        while q[0]<=(r-window_size):
            q.popleft()
        while (r-l+1)>=window_size:
            output.append(nums[q[0]])
            l+=1
        r+=1
    return output

def second_largest_in_subarray():
    size_array=int(input("enter the size of the array: "))
    nums=[]
    for i in range(size_array):
        nums.append(random.randint(1,100))
    for i in range(size_array):
        print(nums[i],end=" ")
    window_size=int(input("enter the size of the window: "))
    second_largest_elements=[]
    q=deque()
    l=0
    for r in range(size_array):
        while q and nums[q[-1]]<=nums[r]:
            q.pop()
        q.append(r)
        while q[0]<=(r-window_size):
            q.popleft()
        if (r-l+1)==window_size:
            
            largest=(nums[q[0]])
            second_largest=float('-inf')
            for idx in q:
                if nums[idx]!=nums[q[0]]:
                    second_largest=max(second_largest,nums[idx])
            second_largest_elements.append(second_largest if second_largest != float('-inf') else None)
            l+=1
    
    return second_largest_elements

def rearrange():
    num=int(input("enter the number"))
    nums=[]
    for i in range(num):
        nums.append(random.randint(-100,100))
    for i in range(num):
        print(nums[i],end=" ")
    pos_index=0
    for i in range(num):
        if nums[i]>0:
            temp=nums[i]
            for j in range(i,pos_index,-1):
                nums[j]=nums[j-1]
            nums[pos_index]=temp
            pos_index+=1

            
    return nums

def is_prime():
    num=random.randint(2,100)
    print(num)
    if (num==2 or num==3):
        print("its a prime")
    if ((num%6)==5) or ((num%6)==1):
        print("its a prime")

    else:
        print("its not an prime number")

def stock_buy_sell():
    noe=int(input("enter the number of elements: "))
    arr=[]
    for i in range(noe):
        arr.append(random.randint(0,100))
    for i in range(noe):
        print(arr[i],end=" ")
    local_minimum=arr[0]
    #local_maximum=arr[0]
    profit=0
    for i in range(1,noe):
        local_minimum=min(local_minimum,arr[i])
        #local_maximum=max(arr[0],arr[i]+1)
        profit=max(profit,arr[i]-local_minimum)
    print()
    return profit

def car_hiring(R1,N,R2,X):
    time_in_hrs=math.ceil(X/60)
    cost=0
    if time_in_hrs>N:
        time_in_hrs-=N
        cost+=time_in_hrs*R2
        cost+=N*R1
    else:
        cost+=time_in_hrs*R1
    return cost

def power_4_check():
    n=int(input("enter the number: "))
    if n<0:
        print("Wrong Input")
    d=len(str(n))
    num=n**4
    str_num=str(num)
    k=len(str_num)
    if n>=0:
        if(int(str_num[k-d:])==n):
            print("True")
        else:
            print("False")

def power_4_no_String(n):
    if n<0:
        return "Wrong Input"
    copy=n
    cnt=0
    while(copy):
        cnt+=1
        copy//=10
    num_power_4=n**4
    ending_digits=num_power_4%(10**cnt)
    if (ending_digits==n):
        return True
    else:
        return False

def push10_multiples(arr):
    n=len(arr)
    index_10=n-1
    for i in range(n-1,-1,-1):
        if arr[i]%10==0:
            temp=arr[i]
            for j in range(i,index_10):
                arr[j]=arr[j+1]
            arr[index_10]=temp
            index_10-=1
    return arr

def unique_element(start_index,end_index):
    unique_elements=[]
    for i in range(start_index,end_index+1):
        copy=i
        res=set()
        is_unique=True
        while(copy):
            digit=copy%10
            if digit in res:
                is_unique=False
                break
            res.add(digit)
            copy//=10
        if is_unique:
            unique_elements.append(i)
    return unique_elements

def string_combination(s1):
    n=len(s1)
    sum=0
    for i in range(0,n):
        res=""
        for j in range(i,n):
            res+=s1[j]
            sum+=int(res)
    return sum
        




if __name__=="__main__":
    start_time=time.time()
    print(start_time)
    end_time=time.time()
    print(end_time)
    time_elapsed=end_time-start_time
    print(time_elapsed)



    #n=int(input("enter the  number: "))
    #arr=[10, 12, 5, 40, 30, 7, 50, 9, 10]
    #start_index=int(input("enter the starting index: "))
    #end_index=int(input("enter the ending index: "))


    #s1=input("enter the message: ")
    #for char_at in s1:
        #if char_at==" ":
            #s1=input("enter a single string: ")
    #if s1.isdigit()==0:
        #s1=input("enter a valid number: ")
#euclidean division    
    #n1=5
    #n2=3
    #if n2>n1:
        #n1,n2=n2,n1
    #while n2:
        #n1,n2=n2,n1%n2
    #print(n1)
        

    #print(n&1)
    #print(string_combination(s1))


    #X=int(input("enter the total time travelled: "))
    #R1=int(input("enter the charge for first N hrs: "))
    #N=int(input("enter the duration for the first charge: "))
    #R2=int(input("enter the duration for the next phase of travel: "))
    #total_travelling_cost=car_hiring(R1,N,R2,X)
    #print(f"total_travelling_cost={total_travelling_cost}")


    #prime=2,3,5,7,2,3,5,7,11,13
    #primes=list(prime)
    #unique_primes=list(set(primes))
    #print(unique_primes)


