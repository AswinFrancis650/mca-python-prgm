class student:
      def __init__(self,m1,m2):
            self.m1=m1
            self.m2=m2
      def total(self):
            return self.m1+self.m2

#operator overloading for '+'
      def __add__(self,other):
            total1=self.total()
            total2=other.total()
            return total1+total2
            
#main program
print("Enter marks of student_1")
m11=int(input("Mark for sub_1:"))
m12=int(input("Mark for sub_2:"))
print("Enter marks of student_2")
m21=int(input("Mark for sub_1:"))
m22=int(input("Mark for sub_2:"))

#object
s1=student(m11,m12)
s2=student(m21,m22)

#calculate individual total
print("Total marks of student_1 = ",s1.total())
print("Total marks of student_1 = ",s2.total())

combinedtotal=s1+s2
print("combined Total  of both students = ",combinedtotal)

