n = int(input().split()[0])
for i in range(n):
    l, s = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    
    ans = ""
    _maxlen = -1
    i = 0
    j = i
    curr = s
    while i < len(arr) and j < len(arr):
      
        if arr[j] >= 0:
            curr += arr[j]
            j += 1
        elif arr[j] < 0:
            if curr >= abs(arr[j]):
                curr -=  abs(arr[j])
                j += 1
            elif curr < abs(arr[j]):
              
                a = i + 1
                b = j 
                if b - a > _maxlen:
                
                    ans = str(a) + " " + str(b)
                    _maxlen = b -a
                curr -= arr[i]      
                i += 1
                
       
    a = i + 1
    b = j 
    if b - a > _maxlen:
    
        ans = str(a) + " " + str(b)
        _maxlen = b -a
  
    if len(ans) > 0:
        print(ans)
    else:
        print(-1)
     