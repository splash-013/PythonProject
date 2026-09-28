# PRINT NUMBERS WITH LOOP
# for i in range(1,21):
#     print(i)

# PRINT NUMBERS WITHOUT LOOP
def number(n):
    if n>20:
        return
    print(n)
    number(n+1)
number(1)