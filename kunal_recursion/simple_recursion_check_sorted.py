def is_sorted(arr):
    if len(arr)==1:
        return True
    if arr[0]>arr[1]:
        return False
    return is_sorted(arr[1:])

print(is_sorted([1,2,3,4,5,6,11,9,10]))
