def rect(m):
    l = m
    p = 4
    q = 5
    for i in range(p):
        if l[i][0] == 1:
            del(l[i][0])
            q = q-1
        if l[i][3] == 1:
            del(l[i][3])
            q = q-1
    for j in range(q):
        if l[3][j]==1:
            del(l[3][j])
    print(m)
                

# Driver Program
M = [[1,0,0,1,1],
	[1,0,0,0,1],
	[1,0,0,1,1],
	[1,1,1,1,1]]

print(rect(M))

# This code is contributed by Soumen Ghosh
