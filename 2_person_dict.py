person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(person)


print(person['children'][1])        #give list an index

print(person['pets']['cat'])        #give dictionary a key

for child in person['children']:
    print(child)

for pet in person['pets']:
    print(person['pets'][pet])

