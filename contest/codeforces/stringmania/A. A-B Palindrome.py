n = int(input().split()[0])
for i in range(n):
    a, b = list(map(int, input().split()))
    s = input().split()[0]
    arr = []
    for c in s:
        arr.append(c)
        if c == "1":
            b -= 1
        elif c == "0":
            a -= 1
    def ispalindrome(a, b, arr):
        i = 0
        j = len(arr) - 1
        while i <= j:
            

            if arr[i] == "1" and arr[j] == "1":
                i += 1
                j -= 1
            elif arr[i] == "0" and arr[j] == "0":
                i += 1
                j -= 1
            elif arr[i] == "0" and arr[j] == "1":
                return -1
            elif arr[i] == "1" and arr[j] == "0":
                return -1
            elif arr[i] == "?" and arr[j] == "?":
                if i == j:
                    if a > 0:
                        arr[i] = "0"
                        a -= 1
                    elif b > 0:
                        arr[i] = "1"
                        b -= 1
                    else:
                        return -1
                else:

                    if a >= 2:
                        arr[i] = "0"
                        arr[j] = "0"
                        a -= 2
                        i += 1
                        j -= 1
                    elif b >= 2:
                        arr[i] = "1"
                        arr[j] = "1"
                        b -= 2
                        i += 1
                        j -= 1
                    elif a < 2 and b < 2:
                        return -1
            elif arr[i] == "1" and arr[j] == "?": 
                if b > 0:
                    arr[j] = "1"
                    b -= 1
                    i += 1
                    j -= 1
                else:
                    return -1
            elif arr[i] == "?" and arr[j] == "1": 
                if b > 0:
                    arr[i] = "1"
                    b -= 1
                    i += 1
                    j -= 1
                else:
                    return -1
            elif arr[i] == "0" and arr[j] == "?": 
                if a > 0:
                    arr[j] = "0"
                    a -= 1
                    i += 1
                    j -= 1
                else:
                    return -1
            elif arr[i] == "?" and arr[j] == "0": 
                if a > 0:
                    arr[i] = "0"
                    a -= 1
                    i += 1
                    j -= 1
                else:
                    return -1
        if a > 0 or b > 0:
            return -1
        else:
            return "".join(arr)
    print(ispalindrome(a, b, arr))




