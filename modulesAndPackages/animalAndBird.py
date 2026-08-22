#Approach 1
# import bird
# import animal
#
# b=bird.Bird() #module name is used to create the object from bird class
# a=animal.Animal() #module_name.class_name
#
# b.b1() #object to call the method
# a.a1() #object_name.method_name

#Approach 2
from bird import Bird #import class
from animal import Animal #import class

Bird().b1()
Animal().a1()




