import random
              #key     value
phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}



print()
print('*****  start section 1 - print dictionary ********')
print()

print(phonebook)                #prints dictionary
print(type(phonebook))          #prints class type (dict)
phone = phonebook['Chris']      #prints value tied to key 'Chris'

print(phone)

mydictionary = {}               #creates empty dictionary
print(mydictionary)

mydictionary = dict(m=8, n=9)   #function 'dict' allows you to create the dictionary (m is key, 9 is value)
print(mydictionary)

print()
print('*****  end section 1 ********')
print()





print()
print('*****  start section 2 - search dictionary ********')
print()

name = 'Chris'

if name in phonebook:           #searches dictionary for key, returns value if found and else if not found
    print(phonebook[name])      
else:
    print(name, "is not in the phonebook")



print()
print('*****  end section 2 ********')
print()



print()
print('*****  start section 3 - edit/append dictionary ********')
print()

print(phonebook)
phonebook['Chris'] = '555-0123'     #sets new value for given key
phonebook['Joe'] = '555-444'
print(phonebook)


print()
print('*****  end section 3 ********')
print()



print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()

#del phonebook['Chris']         #deletes key and value from dictionary    
#print(phonebook)


print()
print('*****  end section 4 ********')
print()



print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()

for key in phonebook:           
    print(key)
    print(phonebook[key])

print()
#default itteration is the keys. It will loop through the keys

for value in phonebook.values():     #call the method values to itterate through all the value
    print(value)

print()

for k,v in phonebook.items():
    print('Key:',k, ' value:',v)

print()

for tuple in phonebook.items():
    print(tuple)
    

print()
print('*****  end section 5 ********')
print()



print()
print('*****  start section 6 - using get and clear ********')
print()


phone = phonebook.get('Chris', 'key not found')
print(phone)

#phonebook.clear()
#print(phonebook)


print()
print('*****  end section 6 ********')
print()



print()
print('*****  start section 7 - using pop method ********')
print()


#a = phonebook.pop('Chris', 'not found')     #searches for key and grabs associated value + deletes from dict

#print(a)

#print(phonebook)


print()
print('*****  end section 7 ********')
print()



print()
print('*****  start section 8 - using popitem ********')
print()

#print(phonebook)
#a = phonebook.popitem()     #removes random item from dictionary

#print(a)

#print(phonebook)


print()
print('*****  end section 8 ********')
print()



print()
print('*****  start section 9 - using random and converting to list ********')
print()

list_of_keys = list(phonebook)
print(list_of_keys)

random_key = random.choice(list_of_keys)
print(random_key)

random_value = phonebook[random_key]
print(random_value)

#alternative shorter method
random_value = phonebook[random.choice(list(phonebook))]
print(random_value)


print()
print('*****  end section 9 ********')
print()








