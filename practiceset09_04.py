#correct inappropriate word by *****
with open ("sample0905.txt","r") as f : 
    content = f.read()
content = content.replace("fuck","****")
with open ("sample0905.txt","w") as f : 
    f.write(content)