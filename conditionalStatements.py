# if, if else, elif

# Type 1
# age=int(input('Enter your age: '))
#
# if age>=18:
#     print("Eligible to vote")
# else:
#     print('Not eligible to vote')

# Type 2 Ternary operator
# print('Eligible to vote') if age>=18 else print('Not eligible to vote')

# Type 3 print multiple statements
# {print('Eligible to vote'), print('Age is above 18')} if age>=18 else {print('Not eligible to vote'), print('Age is below 18')}

# Type 4 elif - used when there are multiple conditions

# day = int(input("Enter no between 1 to 7: "))
#
# if day==1:
#     print('Monday')
# elif day==2:
#     print('Tuesday')
# elif day==3:
#     print('Wednesday')
# elif day==4:
#     print('Thursday')
# elif day==5:
#     print('Friday')
# elif day==6:
#     print('Saturday')
# elif day==7:
#     print('Sunday')
# else:
#     print('Invalid number')

# Check if the given no is positive or negative
# no=int(input('Enter a number: '))
# if no>=0:
#     print("The number is Positive!")
# else:
#     print('The number is Negative!')
#
# # Check the largest of two numbers
no1=int(input('Enter first no: '))
no2=int(input('Enter second no: '))

if no1>no2:
    print('First no is greater')
else:
    print('Second no is greater')

# Check largest of three numbers
