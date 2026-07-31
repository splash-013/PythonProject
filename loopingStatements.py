# Looping statements
# while, for loop

# while -
# initialization
# condition
# increment/decrement

# i=int(input('Enter a number: ')) #initialization
# while (i<=10): #condition
#     print(i)
#     i=i+1 #increment/decrement or i+=1


# for loop
# for i in range(10): #indexing starts form 0 to (n-1)
#     print(i)

# for i in range(1,11):
#     print(i)

#print only even numbers between 1 to 20
# for i in range(0,21,2):
#     print(i)

#print only odd numbers between 1 to 20
# for i in range(1,21,2):
#     print(i)

# break  - immediate stop
# for i in range(100):
#     if (i==45):
#         break
#     print(i)

# continue - skip the condition
for i in range(101):
    if (i==45):
        continue
    print(i)





