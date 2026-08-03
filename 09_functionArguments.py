# def text(name,ending='Thank you'):   #name and ending(default) are parameters
#     #print(f"Good morning, {name}\n{ending}")
#     print(f'Good Morning, {name}')
#     print(ending)
#
# text('Palash') #argument is called

#Example 1
#function definition
# def myFun ():
#     print("'Hello World'")
# myFun() #function call

#Example 2
# def myFun(name): #name is a parameter
#     print('Hello!', name)
#     print(f'Hello! {name}')
# myFun('Palash') #Palash is the argument

#Example 3
# def myFun(name, surname):
#     print(f'Hello! {name} {surname}')
# myFun('Palash', 'Shahare')

#Example 4
# def myFun(surname, name='Palash'): #always put default parameter second and not first
#     print('Hello', name)
#     print(surname)
# myFun('Thank you!!')

#Example 5, return
a=int(input("Enter first number: "))
b=int(input('Enter second number: '))
def sum(a,b):
    return(a+b) #returning a value
x=sum(a,b) #returning a output should be stored in a variable, hence x
print(x)
print(x*2) #storing return value in a variable can be reused






