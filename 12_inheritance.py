#inheritance -
#Acquiring variables and methods from one class to another

#Objective -
#1.Code reusability
#2.Avoid duplicate code

#Types of inheritance -
#-Single
#-Multi level
#-Hierarchial
#-Multiple

# Single Inheritance
# ONE parent ONE child

#Example 1
# class Parent:
#     def M1(self):
#         print("Method from Parent class")
#
# class Child(Parent): #by adding Parent class, child class inherited properties from parent class
#     def M2(self):
#         print("Method from Child class")
#
# Child().M1() #method from Parent class
# Child().M2()

#Example 2 - add variables
# class Parent:
#     a,b=100,200
#     def M1(self):
#         print(self.a+self.b)
#
# class Child(Parent):
#     x,y=300,400
#     def M2(self):
#         print(self.x+self.y)
#         print("Below variables are from Parent class")
#         print(self.a+self.b)
#
# Child().M2()
# # Child().M1()

#Example 3 same method name
# class Parent:
#     def M1(self):
#         print('Parent method')
#
# class Child(Parent):
#     def M1(self):
#         print('Child method')
#         super().M1()  #super defines Parent class, it is used to OVERRIDE Parent methods
#
# Child().M1()

# Example 4 overriding values
class Parent:
    name="John"

class Child:
    name='Palash' #overriding variable

print(Child().name)

















