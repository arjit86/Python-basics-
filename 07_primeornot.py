a = int (input("Enter no a as :"))
b = int (input("Enter no b as :"))
c = int (input("Enter no c as :"))
d = int (input("Enter no d as :"))

eA= 0
n = 0
for i in range (1,a+1): 
    if (a%i==0): 
        n = n + 1 
if (n==2):
    eA=a 

eB=0  
n = 0
for i in range (1,b+1): 
    if (b%i==0): 
        n = n + 1 
if (n==2): 
    eB=b

eC=0
n = 0
for i in range (1,d+1): 
    if (c%i==0): 
        n = n + 1 
if (n==2): 
    eC=c

eD=0
n = 0
for i in range (1,d+1): 
    if (d%i==0): 
        n = n + 1 
if (n==2): 
   eD=d

print (str(eA+eB+eC+eD))