#String Slicing
greet = 'Hello'
# access 1st index element
print(greet[1]) 
greet = 'Hello'
# access character from 1st index to 3rd index
print(greet[1:4])  

#String Compare
str1 = "Python Programming"
str2 = "Information Technology"
str3 = "Python Programming"
# compare str1 and str2
print(str1 == str2)
# compare str1 and str3
print(str1 == str3)

#String concatenate
greet = "Good"
name = "Morning!"
# using + operator
result = greet + name
print(result)

greet = 'Python'
# iterating through greet string
for letter in greet:
    print(letter)
greet = 'Python'
# count length of greet string
print(len(greet))

#Membership Operator
print('a' in 'program') 
print('at' not in 'battle') 
