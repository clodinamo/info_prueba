'''
6-Escribe un programa que pida al usuario una palabra y luego imprima la misma
palabra pero con las letras en orden inverso.
'''

palabra = input("Introduce una palabra: ")
palabra_invertida = palabra[::-1]

print("La palabra invertida es:", palabra_invertida)

#opcion 2
'''
i = -1
while i >= -len(palabra):
print(palabra[i])
i = i - 1
'''