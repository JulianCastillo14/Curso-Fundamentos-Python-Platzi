#las tuplas no me permiten hacer cambios de los elemnetos y esta es la principal diferencia con las listas
numbers = (1, 2, 3, 5)
strings = ('juli', 'santi','karen', 'santi')

print(numbers, type(numbers))
print('0 =>', numbers[0])
print('-1 =>', numbers[-1])
print(strings, type(strings))

#las tuplas tambien me permiten tener diferentes tipos de datos
#CRUD no se puede hacer en tuplas

#Metodos que tienen las tuplas
print(strings)
print(strings.index('juli'))
print(strings.count('santi'))

#si podemos hacer transformaciones pasando de una lista a una tupla 
my_list = list(strings)
print(type(my_list))

my_list[1] = 'claudia'
print(my_list)

#Tambien podemos pasar de una lista a una tupla
my_tuple = tuple(my_list)
print(my_tuple)

