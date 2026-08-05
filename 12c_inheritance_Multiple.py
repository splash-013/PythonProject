# Multiple inheritance
# MANY parent ONE child

class Parent_01:
    a,b=100,200
    def M1(self):
        print(self.a+self.b)
class Parent_02:
    x,y=300,400
    def M2(self):
        print(self.x+self.y)

class Child(Parent_01,Parent_02):
    def M3(self):
        print('Self Method')

#child can access methods from both the parents
Child().M1()
Child().M2()
Child().M3()
