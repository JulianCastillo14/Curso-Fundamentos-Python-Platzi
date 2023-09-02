text = "Ella sabe programar en Python"

'''
print('JavaScript' in text )
print('Python' in text )
if 'JS' in text:
    print('Elegiste bien')
else:
    print('Tambien elegiste bien')

size = len('amor')
print(size)

#Recuerda que los espacios tambien cuentan
size = len('amor    ')
print(size)
'''

size =  len(text)
print(size)

print(text)
print(text.upper()) #mayusculas
print(text.lower()) #minusculas
print(text.count('a')) #contar caracteres
print(text.swapcase()) #cambia minuscualas a mayusculas y mayusculas a minusculas
print(text.startswith('Ella')) #Revisa si un texto comienza con cierta cadena
print(text.endswith('Rust')) #Revisa si un texto termina con cierta cadena 
print(text.replace('Python', 'Go')) #Cambianos una cadena que esta en un texto por otra
text_2 = "este es un titulo"

print(text_2)
print(text_2.capitalize()) #Pone la primera letra de un texto en Mayuscula
print(text_2.title()) #Poner la primera letra en Mayuscula de cada palabra que este dentro del texto
print(text_2.isdigit()) #Nos dice si algo es un digito o si potencialmente lo es 
print('390'.isdigit())