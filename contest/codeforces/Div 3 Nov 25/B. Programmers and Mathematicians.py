n = int(input().split()[0])
for i in range(n):
    a, b = list(map(int, input().split()))
    def team(a, b):
        return min(a, b, (a+b) // 4)
    print(team(a,b))
        
        

        