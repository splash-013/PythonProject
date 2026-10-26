# CONDITIONAL STATEMENTS - IF, IF ELSE, ELIF

# PERSON ELIGIBLE TO VOTE OR NOT
# a=int(input("Enter a number: "))
# if a>=18:
#     print("Eligible to vote")
# else:
#     print("Not eligible to vote")

# EVEN OR ODD NUMBERS
# try:
#     a=int(input("Enter a number: "))
#     if a%2==0:
#         print("Even number")
#     else:
#         print("Odd number")
# except ValueError:
#     print("Invalid value")

# KNOW THE WEEKDAY USING NUMBER
# try:
#     a=int(input("Enter a number: "))
#     if a==1:
#         print("Sunday")
#     elif a==2:
#         print("Monday")
#     elif a==3:
#         print("Tuesday")
#     elif a==4:
#         print("Wednesday")
#     elif a==5:
#         print("Thursday")
#     elif a == 6:
#         print("Friday")
#     elif a == 7:
#         print("Saturday")
#     else:
#         print("Invalid input")
# except ValueError:
#     print("Invalid input")

# CHECK DIVISIBILITY
# 1--> divisible by 2 and 5
# 2--> divisible by 2 but not 5
# 3--> not divisible by 2 but by 5
# 4--> not divisible by 2 and 5
try:
    a = int(input("Enter a number: "))
    if a%2==0:
        if a%5==0:
            print("divisible by 2 and 5")
        else:
            print("divisible by 2 but not 5")
    else:
        if a%5==0:
            print("not divisible by 2 but by 5")
        else:
            print("not divisible by 2 and 5")
except ValueError:
    print("Invalid number")

# a= int(input("Enter a number: "))
# if a%2==0 and a%5==0:
#     print("divisible by 2 and 5")
# elif a%2==0 and a%5!=0:
#     print("divisible by 2 but not by 5")
# elif a%2!=0 and a%5==0:
#     print("not divisible by 2 but by 5")
# else:
#     print("not divisible by 2 and 5")













