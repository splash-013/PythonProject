# import package inside package

#Approach 1
# import sys
# sys.path.append('C:/Users/palash.shahare/PycharmProjects/PythonProject/package_01')
# sys.path.append('C:/Users/palash.shahare/PycharmProjects/PythonProject/package_01/package_02')
# # provide path of package_02 as well to access the class, methods, functions
#
# from module_01 import *
# Display().m1()
# from module_03 import *
# Display().m3()

#Approach 2
import sys
sys.path.append('C:/Users/palash.shahare/PycharmProjects/PythonProject/package_01')
sys.path.append('C:/Users/palash.shahare/PycharmProjects/PythonProject/package_01/package_02')

import module_01 as mod1 #alias name mod1
import module_03 as mod3 #alias name mod3

mod1.Display().m1()
mod3.Display().m3()