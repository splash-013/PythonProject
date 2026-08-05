# import for another package or folder
import sys
sys.path.append('C:/Users/palash.shahare/PycharmProjects/PythonProject/package_01')

from module_01 import *
Display().m1() #same class name in both the modules
from module_02 import *
Display().m2() #same class name in both the modules


