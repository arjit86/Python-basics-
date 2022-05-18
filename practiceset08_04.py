#function to find the multiplication of a given number
def multi(n): 
    for i in range(1,11): 
        print (str(n) + "X" + str(i) +  "=" + str(n*i))
a = int (input("Enter any no : "))
multi (a)