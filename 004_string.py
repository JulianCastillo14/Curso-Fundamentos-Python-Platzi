name = 'Julian'
lastname = 'Castillo'
my_age = 21

template = f"Hola mi nombre es {name}, mi apellido es {lastname} y mi edad es de {my_age} años"
print('v4 =>', template)

full_name = name +' '+ lastname
print(full_name)

quote = "I'm Julian"
print(quote)

quote2 = 'She said "Hello" '
print(quote2)

#format
template = "Hola, mi nombre es " + name + " y mi apellido es " + lastname
print('v1 =>',template)

template = "Hola, mi nombre es {} y mi apellido es {}".format(name,lastname)
print('v2 =>',template)

template = f"Hola, mi nombre es {name} y mi apellido es {lastname}"
print('v3 =>',template)