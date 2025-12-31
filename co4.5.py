class student:
      def __init__(self,name):
          self.name=name
      def display(self):
          print("Name=",self.name)
          
#child class inheriting from parent class
class MCAStudent(student):
      def __init__(self,name,semester):

#call parent class constructor using super()
          super().__init__(name) 
          self.semester=semester
      def showdetails(self):
          self.display()
          print("Semester=",self.semester)

#main program
name=input("Enter the student Name:")
semester=input("Enter the Semester: ")

#object of child class
s=MCAStudent(name,semester)
print("Student Details are:")
s.showdetails()         
