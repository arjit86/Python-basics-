#wap to find out that the word python is in which line 
content = True 
i = 1
with open ("sample0905.txt", "r") as f : 
    while content : 
        content = f.readline()

        if "python" in content.lower(): 
            print (content)
            print (" python is present")
            print (i)
        i=i+1   

                           
                           