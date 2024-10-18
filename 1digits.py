n=int(input("Enter any number"))
tot=0
while(n>0):
      dig=n%10
      tot=tot+dig
      n=n//10
print("total sum of digits is",tot)      
