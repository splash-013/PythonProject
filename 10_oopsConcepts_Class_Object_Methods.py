# create a class
class Employee:  #Employee is the class name, class is the keyword used to create a class
# create methods (functions inside a class are called methods)
    def emp_id(self): #self is used to know that function is related to the Employee class, emp_name is the method name
        pass #none value
    def emp_name(self, name): #name is a parameter
        print(name)
    def emp_location(self):
        print('Pune')

# create objects, specify the class name and add ()
Employee() #Object
Employee().emp_location() #access the methods by the object
Employee().emp_name('Palash') #argument for name parameter
Employee().emp_id()

emp1=Employee() #it can also be stored in a variable
emp1.emp_id() #object call the method
emp1.emp_name('Naruto')
emp1.emp_location()

#emp2=Employee() #object


