def unique_no_builtin(arr):
    """
    ans=set()
    for i in range(len(arr)):
        if arr[i] not in ans:
            ans.add(arr[i])
    return list(ans)
    """
    return list(set(arr))

print(unique_no_builtin([1,2,2,3,3,4,4,5,2,1,34]))