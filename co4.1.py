class student:
      def  __init__(self,name,rollno,marks):
          self.name=name
          self.rollno=rollno
          self.marks=marks
      def display(self):
        print(f"Name={self.name}\nRollno={self.rollno}\nMarks={self.marks}\n")
      
      def updatemarks(self,newmarks):
          self.marks=newmarks
          
name=input("Enter student Name:")
rollno=input("Enter student Roll no:")
marks=int(input("Enter student Marks:"))

#create student object
s1=student(name,rollno,marks)
#display the initial details
s1.display() 

#Update marks
newmarks= int(input("Enter new marks to update:"))
s1.updatemarks(newmarks)
#display updated details
s1.display()
