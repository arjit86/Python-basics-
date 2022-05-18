a = int (input("Enter any number : "))
for i in range (10,0,-1):
    print (str(a) + "*" + str (i) + "=" + str(i*a))
    #or 
    #print (f"{a}X{i}={a*i}")