a=list(map(int, input().split()))
b=set(a)
v=sorted(b)
print(v)
c=len(v)
e=c-2
d=v.pop(e)
print(d)