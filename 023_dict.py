person = {
    'name': 'Julian',
    'last_name': 'Cañon',
    'langs': ['python', 'c++'],
    'age': 21
}

print(person)

person['name'] = 'Jerson'
print(person)
person['age'] += 1
print(person)
person['langs'].append('java')
print(person)

del person['last_name']
person.pop('age')
print(person)

print('items') # Nos devuelve las claves y los valores en pares de tuplas
print(person.items())

print('keys')
print(person.keys()) #Nos devuelve las claves

print('values')
print(person.values()) #Nos devuelve los valores 
