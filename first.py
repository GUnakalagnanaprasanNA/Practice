a='10'
print(a)
print(type(a))

#multiline strings
b='''python
java
C
C++'''
print(b)
print(type(b))

#list
l=[25,36,74,84]
print(l)
print(type(l))
print(l[0])
l.append(200)
print(l)
#l[0].append(300) it give error
print(l)

#tuple
t=(10,20,30,40)
print(t)
print(type(t))

#sets
s={10,20,30,40}
print(s)
print(type(s))
#print(type(s[0])) give error, it doesn't contain any index
s.add(200) #append gives error
print(s)
print(s)
s.remove(200)
print(s)

#DICTIONARY
d={"dennis":"c","james":"java"}
print(d)
print(type(d))
d["brendam"]="javascript"
print(d)
d.pop("brendam")
print(d)