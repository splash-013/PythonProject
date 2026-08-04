# Method vs Constructor
# Method:
# Can be given any name
# Returns a value
# Can have arguments/parameters
# Object is used to invoke a method
#
# Constructor:
# Constructor name is fixed __init__()
# This will not return any value
# This will be called at the time of object creation

#Example 1
# class MyClass:
#     def __init__(self):
#         print('This is a constructor...')
#     def x(self):
#         print('This is a method')
# MyClass().x() #invoke the constructor automatically along with other(x) method

#Example 2 passing parameter through a constructor
class MyClass:
    def __init__(self,name): #name parameter
        print(name)
MyClass('Palash') #object creation invoke the constructor

