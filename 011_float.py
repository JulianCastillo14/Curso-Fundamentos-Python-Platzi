x = 3.3
print(x)
y = 1.1 + 2.2
print(y)
#Podemos observar en consola que da False esto debido a la presición decimal
print(x == y)

#Intentemos arreglar esto

#Forma 1
y_str = format(y,".2g")
print("y_str =>", y_str)
print(y_str == str(x))

print('-'*20)

#Forma 2 
print(y,x)
tolerance = 0.0001
print(abs(x - y) < tolerance)
