def series(n):
    valid = ["0","1","2","5","6","8","9"]
    k = n//7
    d = n-(k*7)
    res = valid[d]
    return (int(k*10+int(d)))


#n = 8
n = int(input())
print(series(n))
