numbers = [ 1, 2, 3 , 4]
print(numbers)
print(type(numbers))


tasks = ['make a dishes', 'play videogames']
print(tasks)

#Las listas no permiten al,acenar varios tipos de datos

types = [1, True, 'hola']
print(types)

print(numbers[0])
print(tasks[0])

text = 'Hola'

tasks[0] = 'watch platzi courses'
print(tasks)

tasks[0] = 'do the dishes'
print(tasks)

print(numbers[:3])
print(True in types)
print('hola' in types)