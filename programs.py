# Find the first repeating character in the string "automation"?
# s = "automation"
#
# for i in range(len(s)):
#     for j in range(i + 1, len(s)):
#         if s[i] == s[j]:
#             print("First repeating character:", s[i])
#             break
#     else:
#         continue
#     break


numbers = [1, 2, 3, 4, 3, 5, 2]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

for num in frequency:
    if frequency[num] > 1:
        print(num)