a = int(input("Enter first number: ")) 
b = int(input("Enter second number:")) 
c = int(input("Enter third number: "))
if a > b and a > c: 
    biggest = a
elif b > c:              
    biggest = b 
else: 
    biggest = c 
if a < b and a < c:           
    smallest = a 
elif b < c: 
    smallest = b 
else: 
    smallest = c 
print("Biggest number:", biggest) print("Smallest number:", smallest) 
