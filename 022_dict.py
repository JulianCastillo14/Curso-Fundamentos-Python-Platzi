my_dict = {}
print(type(my_dict))

my_dict = {
    'name': 'Julian',
    'last_name': 'Cañon',
    'age': 21
}

print(my_dict)
print(len(my_dict))

print(my_dict['name'])
print(my_dict['last_name'])
print(my_dict.get('unvalue')) #Con el get puedo tener un none que me dice si la clave no esta y no me para el programa

print('name' in my_dict)
print('is_single' in my_dict)