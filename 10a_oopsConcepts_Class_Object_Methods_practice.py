# class Student:
#     def stu_id(self,id): #instance method
#         print(id)
#     def stu_name(self,name): #instance method
#         print(name)
#     @staticmethod
#     def stu_location(self,location): #static method
#         print(location)
#
# stu1=Student()
# stu1.stu_id(1313)  #instance method
# stu1.stu_name('Palash')  #instance method
# Student.stu_location('Pune')  #static method, directly called from class

#class variable - variables inside a class
#self.variable_name is used to call the class variable
# class MyClass:
#     a=int(input("Enter first no: ")) #class variable
#     b=int(input("Enter second no: ")) #class variable
#     def sum(self):
#         print(self.a+self.b) #call the class variable using self
#     def multi(self):
#         print(self.a*self.b) #call the class variable using self
# MyClass().sum()
# MyClass().multi()

#Example of all variables
i,j=10,20 #global variables
class Var:
    a,b=30,40 #class variables
    def sum(self,x,y): #local variables x and y
        print(x+y)
        print(self.a+self.b) #access class variables
        print(i+j)
        #print(globals()['i']+globals()['j']) #use if same variable names
Var().sum(50,60)












