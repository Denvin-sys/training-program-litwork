n=int(input())
n=bin(n)
n=n[2:]
n=n.replace("0","x")
n=n.replace("1","0")
n=n.replace("x","1")

d=int(n,2)
print(d)

