for i in range(2,21): 
    with open (f"table of {i}","w") as f :
        for j in range(1,11): 
         f.write(str(i) + "X" + str(j) + "=" + str(i*j))
         f.write("\n")