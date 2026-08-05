# Multi level inheritance

class Parent:
    x,y=100,200
    def M1(self):
        print(self.x+self.y)

class Child_1(Parent):
    def M2(self):
        print(self.x) #variable from Parent class

class Child_2(Child_1): #
    def M3(self):
        print(self.y) #variable from grandparent class accessed through Parent class

Child_2().M1()
Child_2().M2()
Child_2().M3()

