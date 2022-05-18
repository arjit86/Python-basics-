#wap to create the copy of the text file this.txt 
with open("this.txt","r") as f : 
    content = f.read() 
with open ("new.txt","w") as f : 
    f.write(content)