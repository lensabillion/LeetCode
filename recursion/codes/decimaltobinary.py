n = int(input().split()[0])
# def decimaltobinary(n):
#     rem = []
#     while n:
#         rem.append((n % 2))
#         n = n // 2
#     return rem
# print(decimaltobinary(n))

ans = ""
def recur_decimaltobinary(n, ans):
    if n == 0:
        return ans
    ans = str(n % 2) + ans
        
    return recur_decimaltobinary(n//2, ans)


print(recur_decimaltobinary(n, ans))
    