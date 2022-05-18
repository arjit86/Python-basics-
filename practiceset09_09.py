with open ("this.txt","r" ) as f : 
    content1 = f.read() 
with open ("new.txt","r") as f : 
    content2 = f.read() 
if content1 == content2 : 
    print ("They are the files with the same content")
else :
    print ("They are the files with the different content")