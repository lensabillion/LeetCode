arr = list(map(int,input().split()))
def binarysearch(arr, left, right, target):
    if left > right:
        return False
    mid = (left + right) // 2
    if target == arr[mid]:
        return True
    if target < arr[mid]:
        return binarysearch(arr, left, mid-1, target)

    return binarysearch(arr, mid + 1, right, target)
    
print(binarysearch(arr, 0, len(arr), 10))