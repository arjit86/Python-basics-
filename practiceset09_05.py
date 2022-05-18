words = ["arjit","person"]
with open("sample0905.txt","r") as f : 
    content = f.read()

for word in words :
    content = content.replace("word","*****")
    with open("sample0905.txt","w") as f : 
        f.write(content)    