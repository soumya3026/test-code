def subs(s1,s2):
    k = s2[-1]
    n = sum(map(lambda x : x == k, s1))
    return n


#s1 = "going to go to goa"
#s2 = "go"
s1 = input()
s2 = input()
print(subs(s1,s2))
