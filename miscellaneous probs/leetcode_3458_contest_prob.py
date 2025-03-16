def can_generate_k_substring(s,k):
    arr=[[-1,-1] for _ in range(26)] # to store first and last occurence of every character
    for curr_ind in range(len(s)):
        ind=ord(s[curr_ind])-ord('a')
        if arr[ind][0]==-1:
            arr[ind][0]=curr_ind
        arr[ind][1]=curr_ind
    
    to_be_sorted_arr=[]
    
    for element in arr:
        start=element[0]
        end=element[1]
        is_valid=True
        for j in range(start,end+1,1):
            left_ind=arr[ord(s[j])-ord('a')][0]
            if left_ind<start:
                is_valid=False
            end=max(end,arr[ord(s[j])-ord('a')][1])
        if end-start+1<len(s) and is_valid:
            to_be_sorted_arr.append([start,end])

    to_be_sorted_arr.sort(key=lambda x:x[1])
    cnt=0
    end_ind=-1
    for interval in to_be_sorted_arr:
        if interval[0]>end_ind:
            cnt+=1
            end_ind=interval[1]

    return cnt>=k
        
if __name__=="__main__":
    s=input()
    k=int(input())
    print(can_generate_k_substring(s,k))