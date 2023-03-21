a=[10,20,15,70,80]
b=(10,13,15,17,20,100)
print(type(a))
print(type(b))
a[2]=50
print(a)

a.append(200)
print(a)
a.insert(1,777)
print(a)

c=[20,50,70]
a.append(c)
print(a)
len(a)
del(a[7])
print(a)