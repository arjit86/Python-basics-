myDict = {
    "dribble" : "to control the ball" ,
    "score" : "to hit the ball inside the rim" , 
    "foul" : "to play in a rough way and violating the rule ",
    "3 points" : "to score the ball in the ring from the three point line", 
    "2 points" : "to score the ball in the ring from the two points line"

}
a = input ("Enter bb related word : ")
print ("The meaning of word a is ",myDict.get(a))
