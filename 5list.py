#correcting mistake values in alist
odd=[2,4,6,8]
#change the 1st item
odd[0]=1
print(odd)
#change 2nd to 4th items
odd[1:4]=[3,4,7]
print(odd)
#update list
odd[3]=7.5
print(odd)
#delete list
del odd[2]
print("After deleting value at index 1:",odd)
