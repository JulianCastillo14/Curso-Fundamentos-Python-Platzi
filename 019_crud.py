# CRUD  Create, Read, Update y Delete

numbers = [1 , 2, 3, 4, 5] #Create

print(numbers[1]) # Read 

numbers[-1] = 10 #Update
print(numbers)

numbers.append(700)#Inserta al final de la lista 
print(numbers)

numbers.insert(0, 'hola') #Con insert lo podemos insertar en una posición deseada
print(numbers)

numbers.insert(3, 'change')
print(numbers)

tasks = ['todo 1', 'todo 2', 'todo 3']

new_list = numbers + tasks
print(new_list)

#Para saber en que posición esta un elemento index
index = new_list.index('todo 2')
new_list[index] = 'todo changed'
print(new_list)

new_list.remove('todo 1')
print(new_list)

new_list.pop() #elimina el ultimo elemento de la lista
print(new_list)

#le puedo enviar una posicion al pop 
new_list.pop(0)
print(new_list)

#para volterar toda la lista al reves  
new_list.reverse()
print(new_list)

#para ordenar una lista
numbers_a = [1, 4, 6, 3]
numbers_a.sort()
print(numbers_a)

strings = ['re', 'ab', 'ed']
strings.sort()
print(strings)

#sort no funciona para listas con datos de diferentes tipos 