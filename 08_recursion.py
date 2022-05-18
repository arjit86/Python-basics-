#factorial.py 
# 5! = 1 * 2 * 3 * 4 * 5
#5! = [1*2*3*(n-1)] * 5 
#5! = (n-1)! * 5
def factorial_recursive(n):
    if (n==1) or (n==0): 
        return 1
    return n * factorial_recursive(n-1)

n = int(input("Enter any no as :"))
print ("The fcatorial of n is : ",factorial_recursive(n))

"""
facto(4)
4 * facto (3)
4 * 3 * facto(2)
4 * 3 * 2 * facto(1)
4 * 3 * 2 * 1 (since when i == 1 it returns 1)


"""