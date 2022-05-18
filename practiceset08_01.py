def gtst(a,b,c): 
    if a > b and a > c : 
        print ("a is the greatest")
    elif b>a and b>c : 
        print ("b is the greatest")
    else : 
        print ("c is the greatest")

c = int (input ("Enter no a as :"))

d = int (input("Enter no b as :"))
e = int (input ("Enter no c as :"))
gtst(c,d,e)