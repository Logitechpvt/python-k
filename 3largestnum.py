print("enter three number")
n1=input()
n2=input()
n3=input()
if(n1>=n2)and(n1>=n3):
   largest=n1
elif(n2>n1)and(n2>=n3):
   largest=n2
else:
    largest=n3
print("the largest number is",largest)
   
