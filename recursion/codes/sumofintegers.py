n = int(input().split()[0])
def sumall(n):
    if n <= 1:
        return n

    return n + sumall(n-1)
print(sumall(n))