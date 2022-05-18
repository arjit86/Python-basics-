#use open function to read the contents of the file
a = open ("arjit.txt","r")#by default the mode is r 
b = a.read(5)#reads the first five characters from the file 
a.close()