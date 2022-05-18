n = 0
a = int(input("enter any no as :"))
for i in range (1,a+1): 
    if (a%i==0): 
        n = n + 1 
if (n==2): 
    print ("It is a prime numbr")
else : 
    print ("It is not a prime number ")
