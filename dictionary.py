dictionai={
    "cat" :  "is cat",
    "dog" : "is dog",
    "elephunt" : "is elephunt",
    "tiger" : [0,1,4,5,6],
    1:2,
    # also you can make adictionary inside a dictionary too#
    #eg
    "anotherdict" : {"koala" : "looks like a panda"}
}
#also mutable
# this means that values can be assigned like in LISTS:
# eg
dictionai["cat"]=(43,42) #in LISTS
# or
dictionai["dog"]=[343,343] #in TUBLES
print(dictionai["cat"])
print(dictionai["dog"])     
print(dictionai["dog"])
print(dictionai["elephunt"])
print(dictionai["tiger"])
print(dictionai["anotherdict"])       #nested lists
print(dictionai["anotherdict"]["koala"])


# keys
print(dictionai.keys()) #dictionary keys are the values or the assets of a dictionary in LISTS format
'(but belongs in the type dict.keys and not lists)'
# can be converted into a list using typecasting
print(list(dictionai.keys()))
print(list(dictionai.values()))
print(dictionai.items()) #gives IN TUPLE FORMAT ##GIVES THE (key,value) for all contents of the dictionary
#gives the values intead of main

'''updating the dictionary'''

print(dictionai)
updatedict0 = {
  "ololololo" : "hulolololo",
  "elephunt" : "likes to hololoololololo" #updates the already existing elephunt 
}
dictionai.update(updatedict0) #updates the dictionary
print(dictionai)

#another one
print(dictionai.get("elephunt"))      #difference                        
print(dictionai["elephunt"])          #isnt present here                 
print(dictionai.get("chapati"))     #here lies                          ###returns none  
print(dictionai["chapati"])          #the difference                     ###invalid