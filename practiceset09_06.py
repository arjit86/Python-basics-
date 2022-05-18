#wap to find out that the word python is present in the file or not
with open ("sample0905.txt", "r") as f : 
    content = f.read().lower() 
    if "python" in content : 
        print ("Python is in the file")  
    else : 
        print ("Python is not in the file")