n = int(input().split()[0])
for i in range(n):
    digit = input().split()[0]
    def evenexist(digit):
        for i in digit:
            if int(i) % 2 == 0:
                return True
        return False
    def makeiteven(digit):
        if int(digit[-1]) % 2 == 0:
            return 0
        elif int(digit[-1]) % 2 != 0 and int(digit[0]) % 2 == 0:
            return 1
        elif int(digit[-1]) % 2 != 0 and int(digit[0]) % 2 != 0:
            if evenexist(digit):
                return 2
            else:
                return -1
    print(makeiteven(digit))