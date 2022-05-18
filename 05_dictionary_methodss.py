myDict = {
    "arjit" : "god" , # here arjit is a key and god is the value associated with it 
    "list" : [1,2,3,4] ,
    "mynumber" : 9869412686
}
# Dictionary methods
print (myDict.keys())#prints all the keys of the dictionary
print(list(myDict.keys()))#listing all the valuess ofn the dictionary 
print ("The values in the Dict are", myDict.values())#values in MyDict
print(myDict.items())#prints the item along with the keyvalues 
print(myDict) 
updateDict = {
    "stepen curry" : "A basketball player"
}
myDict.update(updateDict) #updating the list 
#or 
myDict["magar"]= "surname"
print(myDict)

#difference between .get and non .get
print (myDict.get("arjit"))#it prints even we enter arjit2 
print (myDict["arjit"])#it throws error if we use arjit2 
#to prevent the key error we use .get 
#more methods available in docs.python.org 
