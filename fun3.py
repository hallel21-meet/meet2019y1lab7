print("*")
print("*")
print("*")
print("*")
print("*")

c1 = "@"
c2 = "$"
def stars(n,c):
    print(c * n)
    return ""
print(stars(5,"*"))
print(stars(9,"&"))
print(stars(15,"%"))
print(stars(21,c1))
print(stars(6,c2))

def rec(a,b,c):
    for st in range(a):
        stars(b,c)
    return ""

print(rec(2,11,"^"))

    
