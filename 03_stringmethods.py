a = "arjit"
b = 'magar'
c = '''arjit'''
#all of them are strings
''' 
incase if you have to print arjit's 
You will have to use ""
and use it similar to another conditions
'''

print (type(a))
c = a + b
print ("My name is" + a )
print (c)
print (a[0])
print (a[1])
#note the values of the strings can't be chnaged 
# str[1] = a
#---------------------------------------------------
print(a[0:5]) #3 is excluded ie 0 - 4
# or a[:5]
#negative index 
print (a[-1])
#----------------------------------------------------
print(a[0:])
# or print(a[0:5]) where 5 is excluded
#-----------------------------------------------------
print (a[-5:0])
#index in the form of positive and negative 
# a  r  j  i  t 
# -5 -4 -3 -2 -1
# 0  1  2  3  4
#______________________________________________________

#slicing with the skip value 
print("Skipping the values by using the skip value 2")
#in the string arjit the result will be ajt (r & i will be skippped)
print (a[0:5:2])
#_______________________________________________________________________
arjit = "my name is arjit" 
print (len(arjit))
print (arjit.endswith("arjit"))
print(arjit.count("t"))
print (arjit.capitalize())
print(arjit.find("arjit"))
print(arjit.replace("arjit","suzu"))
