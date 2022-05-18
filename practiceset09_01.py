f = open("poems.txt","r")
a = f.read()
if "twinkle" in a : 
    print ("twinkle is present in it ")
else : 
    print("twinkle is not present in it ")
f.close()