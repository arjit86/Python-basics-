sub1 = int(input("Enter marks one :"))
sub2 = int(input("Enter marks two :"))
sub3 = int(input("Enter marks three :"))
if (sub1<33 or sub2<33 or sub3<33): 
    print("You have failed the exam")
elif(sub1+sub2+sub3)/3 < 40 : 
    print ("You are fail")
else : 
    print("You have passed the exam")