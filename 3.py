def series(n):
    valid = ["0","1","2","5","6","8","9"]
    count = 0
    p = 1
    while(count < n):
        for i in str(p):
            f = 1
            if i not in valid:
                f = 0
            if f==1:
                count += 1
        p += 1
    return p


#n = 8
n = int(input())
print(series(n))
