#Dictionary works in key:value pair

i={
    'Name':'Palash',
    'Age':30,
    'Roll no':13,
    'City':'Pune'
}

j={} #empty dictionary
print(type(j))

# print(type(i))
# print(len(i))
# print(i['Age'])
# print(i.get('City'))
# i['Country']='China'
# print(i)
# if 'Name' in i:
#      print("Key present")
# else:
#      print('Key not present')

#add items
i['Contact']=9545
print(i)

#Difference between
print(i.get('Contact')) #prints none if key does not match

print(i['Contact']) #gives an error if key does not match

#update
# i.update({'Contact':8282})
# print(i)

#remove item
# del i['Contact']
# print(i)




