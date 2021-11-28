arr = list(map(int, input().split()))


def merge(arr, start, mid, end):
    temp = [0] * (end- start + 1)
    i = start
    j = mid + 1
    k = 0
    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
            k += 1
        else:
            temp[k] = arr[j]
            j += 1
            k += 1
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1
    while j <= end:
        temp[k] = arr[j]
        j += 1 
        k += 1
    i = start
    while i <= end:
        arr[i] = temp[i-start]
        i += 1
def mergesort(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        mergesort(arr, start, mid)
        mergesort(arr, mid + 1, end)
        merge(arr, start, mid, end)
mergesort(arr, 0, len(arr)-1)
print(arr)
