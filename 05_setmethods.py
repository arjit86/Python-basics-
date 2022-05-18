b = set() 
print (type(b))
b.add(1)#adding elements in a set 
b.add(2)
print (b)
#note : list & dictionaries  cant be added to set but tuples can be 
b.add((0,1,2))
print (b)
6
print (b.remove(1))#remove any element on set ie remove 1 
# print (b.remove(12))throws an error
print (b)

print (b.pop())#remove anything randomly

c = {1,2,3,4}
print(c.union({2,5}))# c={1,2,3,4} U {2,5}

print (c.intersection({2,5})) # c={1,2,3,4} intersection {2,5}

print (c.clear())