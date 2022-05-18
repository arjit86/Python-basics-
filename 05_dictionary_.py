myDict = {
    "fast" : "In a quick way",
    "arjit" : "A name of the god" ,
    "list" : ["collection","of","smt"], 
    "dict2": {'arjit':'a random coder'}

}
print (myDict['arjit'])
print (myDict['list'])
print (myDict['dict2']['arjit'])#using the multiple dictionary 
myDict["list"] = [1,2,3,4,5] #here we changed the value of the list
print("The value of list is",myDict["list"])