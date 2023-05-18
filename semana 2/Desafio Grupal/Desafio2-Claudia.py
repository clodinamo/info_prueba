#EJERCICIO N°1
# Declaro las variables y le pido al usuario que las dijite.
frase = input("Ingrese una frase o texto: ")
letra1 = input("Ingrese su primera letra: ")
letra2 = input("Ingrese su segunda letra: ")
letra3 = input("Ingrese su tercera letra: ")

# Convierto el texto o frase a minusculas.
frase = frase.lower()
# Armo una lista que almacena la cantidad de veces que se repiten las letras digitadas (tambíen las transformo a minúsculas).
lista_letras_repetidas = [frase.count(letra1.lower()), frase.count(letra2.lower()), frase.count(letra3.lower())]

# Imprimo en pantalla la cantidad de veces que se repite cada una.
print(f"La letra {letra1} se repite {lista_letras_repetidas[0]} veces")
print(f"La letra {letra2} se repite {lista_letras_repetidas[1]} veces")
print(f"La letra {letra3} se repite {lista_letras_repetidas[2]} veces")

#EJERCICIO N°2
# Se nos pide determinar la cantidad de palabras de nuestra cadena de caracteres.
# Creamos una lista separando en strings.
lista_palabras = frase.split()

# Definimos una nueva variable que nos de la cantidad de elementos de la lista anterior.
cantidad_palabras = len(lista_palabras)

#Imprimo en pantalla lo obtenido.
print(f"La cantidad de palabras que hay en el texto es: {cantidad_palabras}")

#EJERCICIO N°3
# En este ejercicio se nos pide devolver la primera y la ultima letra de una cadena de caracteres.
# De esta manera pido que devuelva el primer y último elemento de mi cadena de caracteres.
primera_letra = frase[0]
ultima_letra = frase[-1]

# Imprimo en pantalla.
print(f"La primera letra de su texto es {primera_letra} y la ultima letra es {ultima_letra}")

#EJERCICIO N°4
# En este ejercicio se nos pide mostrar todo el texto en orden inverso.
# Lo hacemos con la funcion reverse, pero primero debemos convertir el str a lista (porq la funcion reverse se aplica a listas)
# Entonces usamos split
texto_inverso = frase.split(" ")
# Ahora si aplicamos reverse
texto_inverso.reverse()
#Definimos otra variable para genear un ciclo (for)
salida = ""

#Generamos un ciclo o bucle
for palabra in texto_inverso:
    salida += palabra +' '

#Imprimimos el resultado en pantalla
print(f'El texto en orden inverso es: {salida}')

#EJERCICIO N°5
# Definimos una funcion, que va a tomar 2 variables str y devolver un bool, una de ellas es frase
def contiene_palabra(frase: str, buscar_palabra: str) -> bool:
    if buscar_palabra in frase:
        return True
    else:
        return False

# Armamos un diccionrio con las respuestas que se van a mostrar en pantalla, la clave es un bool y el valor un str
respuesta: dict[bool, str] = {
    True: "Contiene la palabra python",
    False: "No continene la palabra python"
}


#Imprime el resultado, para eso usamos el metodo get de los diccionarios que busca una clave y nos devuelve su valor
print(respuesta.get(contiene_palabra(frase, "python")))
