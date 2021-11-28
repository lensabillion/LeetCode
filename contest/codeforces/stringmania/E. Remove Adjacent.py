import heapq
n = int(input().split()[0])
s = input().split()[0]
arr = []

cnt  = 0
for i in s:
    arr.append(i)
def addtoheap(arr, heap):
    for c in range(len(arr)):
        heapq.heappush(heap,(-1*( ord(arr[c])-ord('a')), c))
heap = []
addtoheap(arr, heap)
while arr:
    print(heap, cnt)
    val, ind = heapq.heappop(heap)
    val = val * -1
    if 0 < ind < len(arr)-1:
        if abs(ord(arr[ind-1] ) - val) == 1 or abs(ord(arr[ind+1] ) - val) == 1:
            arr = arr[:ind] + arr[ind+1:]
            cnt += 1
            addtoheap(arr, [])
print(cnt)