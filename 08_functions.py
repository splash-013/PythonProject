# functions is a set of code which contains some logic to perform an operation

#logic
# a=int(input("Enter a first no: "))
# b=int(input("Enter a second no: "))
# c=int(input("Enter a third no: "))
# avg=(a+b+c)/3
# print(avg)

#function definition - logic behind the function
# def avg():   #avg() is function name
#     a = int(input("Enter a first no: "))
#     b=int(input("Enter a second no: "))
#     c=int(input("Enter a third no: "))
#     average=(a+b+c)/3
#     print(average)
#
# avg()  #function call  - it can be called n number of times in a program

#GLOBAL and LOCAL variables
#Example 1
# globalVariable=20 #outside the function, can be accessed from anywhere
#
# def fun1():
#     localVariable=40 #inside the function, can be accessed only inside the function
#     print(f"Local variable is {localVariable}")
#     print(f'Global variable is {globalVariable}')
# fun1()

#if the g and l variable names are same, the function will consider only the local variable

#Example 2
# def text():
#     global a
#     a=100
#     print(a)
# text()
#
# print(a) #thought global variable is defined inside the function, it is global and can be accessed from anywhere












