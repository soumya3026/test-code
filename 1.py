def base3(n):
    sig = '-' if n<0 else ''
    n = abs(n)
    if n<3:
        return int(n)
    p = ""
    while(n!=0):
        p += str(n%3)
        n = n//3
    return (sig+str(int(p)))

#n = 10
n = int(input())
print(base3(n))
