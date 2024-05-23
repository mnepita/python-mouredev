'''
Python Variable Name Rules

A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (firstname, Firstname, FirstName and FIRSTNAME) are different variables)
'''
# creacion de una variable - en miniscula y snakeCase

my_str_var = "my string var"
print((my_str_var))

my_int_var = 6
print(my_int_var)
print(type(my_int_var))

bool_var = True
print(bool_var)

print(my_str_var, my_int_var, bool_var)  # pasarle diferentes variables separados por coma ( , )


#concat de variables en un print
print(my_str_var, bool)
print("este es el valor de :", bool_var)

#Funciones del sistema
(print(len(my_str_var)))

# variables en una sola linea 
name, surname, alias, age = "Bruce", "Wayne", "Batman", 33
print("Hola mi nombre es", name, surname, ", y me conocen como", alias, "y tengo", age, "anios de edad")

