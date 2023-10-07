numeros=[10, 20, 30, 40, 50, 60]
n=[3, 4, 5]
c=['L','u', 'i', 's']
s="Mona lisa"
 
suma_numeros = 0
for numero in numeros:
    suma_numeros += numero


producto_n = 1
for num in n:
    producto_n *= num


cadena_c = ''.join(c)


print("Suma de números:", suma_numeros)
print("Producto de números en 'n':", producto_n)
print("Cadena de caracteres:", cadena_c)
print("El cuadro de DA VINCI es:", s.upper())

