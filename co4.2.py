class students:
      def __init__(self,name,mark1,mark2):
          self.name=name
          self.mark1=mark1
          self.mark2=mark2
      def total(self):
          return self.mark1+self.mark2
          
name=input("Enter student Name:")
mark1=int(input("Enter student Mark1:"))
mark2=int(input("Enter student Mark2:"))
#Create object
s1=students(name,mark1,mark2)
print("Total Marks=",s1.total())
