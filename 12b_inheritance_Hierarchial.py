# Hierarchy inheritance
# ONE parent MANY child

class Parent:
    x,y=100,200
    def M1(self):
        pass

class Child_01(Parent):
    a,b=500,600
    def M2(self):
        print(self.x+self.y)
class Child_02(Parent):
    def M3(self):
        print(self.x-self.y)
        # print(self.a+self.b) # cannot access variables from Child_01 as they are not related

Child_01().M3() #Object cannot access method from Child_02 as they are not related
Child_02().M3()

