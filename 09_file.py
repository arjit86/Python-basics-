#use open function to read the contents of the file
a = open ("arjit.txt","r")#by default the mode is r 
b = a.read()
print (b)
a.close()