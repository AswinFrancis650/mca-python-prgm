class rectangle:
     def __init__(self,length,breadth):
         self.length=length
         self.breadth=breadth
         
     def area(self):
         return self.length*self.breadth
         
#operator overloading for '<'
     def __lt__(self,other):
              return self.area()<other.area()
              
print("Enter the Measurements of first rectangle")
l1=int(input("Enter the length of 1st rectangle:"))
b1=int(input("Enter the breadth of 1st rectangle:"))
print("Enter the Measurements of second rectangle")
l2=int(input("Enter the length of 2nd rectangle:"))
b2=int(input("Enter the breadth of 2nd rectangle:"))

r1=rectangle(l1,b1)
r2=rectangle(l2,b2)
print(f"Area of 1st rectangle={r1.area()}\nArea of 2nd rectangle={r2.area()}")
if r1<r2:
   print("First rectangle area is smaller than the second")
else:
   print("First rectangle area is larger than the second")
