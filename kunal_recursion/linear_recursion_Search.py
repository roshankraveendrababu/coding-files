def search_target(arr,target):
    answer=[]
    return helper1(arr,target,0,answer)

def helper1(arr,target,pos,answer):
    if pos>=len(arr):
        return -1 if not answer else answer
    if arr[pos]==target:
        answer.append(pos)
    return helper1(arr,target,pos+1,answer)

# this code aims to not pass the answer array as an parameter
def search_target_no_params(arr,target):
    return helper2(arr,target,0)

def helper2(arr,target,pos):
    if pos>=len(arr):
        return []
    answer=[]
    if arr[pos]==target:
        answer.append(pos)
    below_ans=helper2(arr,target,pos+1)
    return answer+below_ans

if __name__=="__main__":
    arr=input("enter the values: ")
    arr=list(map(int,arr.split()))
    print(search_target_no_params(arr,18))