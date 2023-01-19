
# 1) Boolena Values
is_hungry = True
has_freckles = False

print(is_hungry)
print(has_freckles)

# 2) Numbers Values
age = 35 # integer number
weight = 160.57 # float number

print(age)
print(weight)

# 3) Sring Values
name = "John Doe"
print(name)

# 4) Lists
ninjas = ['Rozen', 'KB', 'Oliver']
print(ninjas)
print(ninjas[1])
print(ninjas[-3])
ninjas.append('Charlie')
print(ninjas)
print(ninjas.pop(2))
print(ninjas)

# 5) Diccionarios
new_person = {
    'name': 'John', 
    'age': 38, 
    'weight': 160.2, 
    'has_glasses': False
}


print(new_person)
print(new_person['name'])
print(new_person['age'])
new_person['skills'] = ['reading', 'swimming', 'karate'] 
print(new_person)
print(new_person['skills'])
new_person['number_of_friends'] = 20;
print(new_person)
new_person['address'] = {
    'street':'my_street_avenue',
    'number': '123456',
    'state': 'XYZ'
}
print(new_person)
print(new_person['address'])

# 6) Common Functions

# 6.1) type()
print(type(is_hungry)) # bool
print(type(name)) # str
print(type(age)) # int
print(type(new_person)) # dict

# 6.2) len()
print(len(name)) # 8 ('John Doe')
print(len(ninjas)) # 3
print(len(new_person)) # 7
print(len(ninjas[1])) # 5 ('KB')
print(len(new_person['address'])) # 3
print(len(new_person['skills'])) # 3
print(len(new_person['address']['number'])) # 6 (123456)
print(len(new_person['skills'][0])) # 7 ('reading')

print(len('Coding Dojo')) # 11