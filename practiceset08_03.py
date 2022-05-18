#sum of nth natural numbers
def sum(n): 
    if (n==0) or (n==1):
        return 1 
    return n + sum(n-1)
a = int(input ("Enter the nth term : "))
print ("The sum is ",sum(a)) 