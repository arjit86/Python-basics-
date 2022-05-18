def greet(name): 
    print ("Hello ! " + name )

name = input ("Input ur name")
greet (name)

def sum(a,b): 
    return a + b 
c = int (input("Enter c :"))
d = int (input("Enter d :"))
print("The sum is :",sum(c,d))

#default value
def hi(name = "arjit"): 
    print ("Hell0 ! " + name )
hi ()
#####################################