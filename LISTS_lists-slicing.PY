# list in python:
#  using []
a=[1,2,3,4,5,6,7]
# a[0]=48 
print(a[0:5])


# SORTING LISTS 
# "sorting is weird compared to letter"
L1=[ 9 , 6 , 1 , 2 , 3 , 57 ]
L1.sort()  # <==this part
L1.reverse()  # <==this part
L1.append(45)  # <==this part     adds at the end of the list     #highly useful
L1.insert(0,3)  
'''on 0th postion 3 will be added'''
L1.insert(2,144)  
'''on 2nd postion 144 will be added'''
L1.pop(2) #2nd postion element will be removed
L1.remove(57) #the element will be removed
print(L1)
