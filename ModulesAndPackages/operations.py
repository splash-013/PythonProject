#Approach 1
# import calculatorFunctions
# calculatorFunctions.add() #module name is to be added
# calculatorFunctions.sub()

#Approach 2
# from calculatorFunctions import add,sub #specific functions/methods that are to be used
# add()
# sub()

#Approach 3
# from ModulesAndPackages.calculatorFunctions import * #import all the functions/methods or class
# import calculatorFunctions2
# add()
# sub()
# calculatorFunctions2.multi()
# calculatorFunctions2.divide()

#Approach 4
#if both the modules have same name methods/functions
from calculatorFunctions import *
add()
sub()
from calculatorFunctions2 import *
multi()
divide()


