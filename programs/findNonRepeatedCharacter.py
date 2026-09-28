s="automation"
#s=[1,2,3,2,4,1,5]
# for i in range(len(s)):
#     count=0
#     for j in range(len(s)):
#         if s[i]==s[j]:
#             count+=1
#     if count==1:
#         print("The first non repeated character:",s[i])
#         break

for i in range(len(s)):
    for j in range(i+1,len(s)):
        if s[i]==s[j]:
            print("Repeated value:",s[i])
            break
        else:
            continue
    break



