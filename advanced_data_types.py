print("------------LISTS    []  ---------------")
lst=[23,56,78,45]
print(lst)
print(type(lst))
l=[10,99.9,"python",True] #heterogenous data
print(l)
print(type(l))
print(lst[0])#23
print(lst[-4])  #  23  (negative indexs is also there)

#  0  1  2   3 ---> postive indexes
#  23 56 78 45 
#  -4 -3 -2 -1   ---> negative indexes

# append -- insert at end 
lst.append(200)
print(lst)  # [23, 56, 78, 45, 200]

#remove
lst.remove(200)
print(lst)   # [23, 56, 78, 45]
print("===========================================")

print("--------------------TUPLE ()  -----------------")
t=(10,99.9,"python",True)
print(t)
print(type(t))
print(t[0])
print(t[-4])  # negative indexs is also there

# append -- insert at end 
#t.append(200) ----> gives error
#print(lst)  
#remove
#t.remove(200) ----> gives error
#print(t)   
print("============================================")

print("--------------------SETS {} -----------------")
s={10,20,30,40}
print(s)
print(type(s))
#add
s.add(200)
print(s)
#remove
s.remove(200)
print(s)
# DUPLICATES NOT ALLOWED
s.add(200)
print(s)
s.add(200)
print(s)
s1={'a',10,"python",99.9,True} #heterogenous data
print(s1)
print(type(s))
print("============================================")

print("--------------------Dictonary  {key:value}-----------------")
d={"dennis":'C',"james": "java","guido":"python"}
print(d)
print(type(d))

#adding
d["brenden"]="javascript"
print(d)
#pop
d.pop("brenden")
print(d)
#DUPLICATES NOT ALLOWED
d["dennis"]="C"
print(d)

d1={'a':10,'b':"python",'c':99.9} #heterogenous data
print(d1)

print("========================================================")


