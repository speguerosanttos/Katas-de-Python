#1.Escribe una función que reciba una cadena de texto como parámetro y devuelva un 
# diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.

def contar_frecuencias_letras(cadena: str) -> dict:
    frecuencias = {}
    for caracter in cadena:
        if caracter != ' ':
            letra = caracter.lower()
            frecuencias[letra] = frecuencias.get(letra, 0) + 1
    return frecuencias

resultado = contar_frecuencias_letras("Hola Mundo")
print(resultado)

#2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()

def obtener_lista_doblada(lista: list) -> list:
    return list(map(lambda x: x * 2, lista))

numeros = [1, 2, 3, 4]
resultado = obtener_lista_doblada(numeros)
print(resultado)

#3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros.
# La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

def filtrar_por_palabra_objetivo(lista_palabras: list, palabra_objetivo: str) -> list:
    return [palabra for palabra in lista_palabras if palabra_objetivo in palabra]

palabras = ["perro", "gato", "gatito", "tigre", "gatera"]
resultado = filtrar_por_palabra_objetivo(palabras, "gat")
print(resultado)

#4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()

def diferencia_entre_listas(lista1: list, lista2: list) -> list:
    return list(map(lambda x, y: x - y, lista1, lista2))

a = [10, 20, 30]
b = [1, 2, 3]
resultado = diferencia_entre_listas(a, b)
print(resultado)

#5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. 
# La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado. 
# Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media y el estado.

def evaluar_nota(lista_numeros: list, nota_aprobado: float = 5) -> tuple:
    media = sum(lista_numeros) / len(lista_numeros) if lista_numeros else 0
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return media, estado

notas = [4, 6, 5, 7]
resultado = evaluar_nota(notas)
print(resultado) 

#6. Escribe una función que calcule el factorial de un número de manera recursiva.

def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(7))

#7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

def tuplas_a_strings(lista_tuplas: list) -> list:
    return list(map(str, lista_tuplas))

tuplas = [(1, 2), (3, 4), (5, 6)]
resultado = tuplas_a_strings(tuplas)
print(resultado)

#8. Escribe un programa que pida al usuario dos números e intente dividirlos. 
# Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada. 
# Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no

def dividir_numeros():
    try:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        resultado = num1 / num2
    except ValueError:
        print("Error: Debes introducir un número válido.")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
    else:
        print(f"La división fue exitosa. Resultado: {resultado}")

dividir_numeros()

#9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista 
# excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es 
# ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()

def filtrar_mascotas(lista_mascotas: list) -> list:
    mascotas_prohibidas = {"Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"}
    return list(filter(lambda mascota: mascota not in mascotas_prohibidas, lista_mascotas))

mascotas = ["Perro", "Gato", "Tigre", "Cocodrilo", "Conejo"]
resultado = filtrar_mascotas(mascotas)
print(resultado)


#10. Escribe una función que reciba una lista de números y calcule su promedio. 
# Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.

class ListaVaciaError(Exception):
    pass

def calcular_promedio(lista_numeros: list) -> float:
    if not lista_numeros:
        raise ListaVaciaError("La lista está vacía, no se puede calcular el promedio.")
    return sum(lista_numeros) / len(lista_numeros)

try:
    promedio = calcular_promedio([])
except ListaVaciaError as e:
    print(f"Error: {e}")
else:
    print(f"El promedio es {promedio}")


#11. Escribe un programa que pida al usuario que introduzca su edad. 
# Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado 
# (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.

def pedir_edad():
    try:
        edad = int(input("Introduce tu edad: "))
        if edad < 0 or edad > 120:
            raise ValueError("La edad debe estar entre 0 y 120.")
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print(f"Edad válida: {edad}")

pedir_edad()


#12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

def longitudes_palabras(frase: str) -> list:
    palabras = frase.split()
    return list(map(len, palabras))

frase = "Hola mundo desde Python"
resultado = longitudes_palabras(frase)
print(resultado)


#13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. 
# Las letras no pueden estar repetidas. Usa la función map()

def letras_may_min(caracteres: str) -> list:
    letras_unicas = set(caracteres.lower())
    return list(map(lambda c: (c.upper(), c.lower()), letras_unicas))

resultado = letras_may_min("aAbBcC")
print(resultado)  


#14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter()

def filtrar_por_letra(lista_palabras: list, letra: str) -> list:
    return list(filter(lambda palabra: palabra.startswith(letra), lista_palabras))

palabras = ["gato", "perro", "gorila", "ratón"]
resultado = filtrar_por_letra(palabras, "g")
print(resultado)


#15. Crea una función lambda que  sume 3 a cada número de una lista dada.

sumar_tres = lambda lista: list(map(lambda x: x + 3, lista))

numeros = [1, 2, 3, 4]
resultado = sumar_tres(numeros)
print(resultado)


#16.  Escribe una función que tome una cadena de texto y un número entero n como parámetros y 
# devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter()

def palabras_largas(texto: str, n: int) -> list:
    palabras = texto.split()
    return list(filter(lambda palabra: len(palabra) > n, palabras))

frase = "La programacion en Python es muy divertida"
resultado = palabras_largas(frase, 6)
print(resultado)


#17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. 
# Por ejemplo, (5,7,2) corresponde al número quinientos setenta y dos (572). Usa la función reduce()

from functools import reduce

def lista_a_numero(digitos: list) -> int:
    return reduce(lambda x, y: x * 10 + y, digitos)

resultado = lista_a_numero([5, 7, 2])
print(resultado) 


#18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes 
# (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90.
# Usa la función filter()

def filtrar_estudiantes(estudiantes: list) -> list:
    return list(filter(lambda e: e["calificacion"] >= 90, estudiantes))

estudiantes = [
    {"nombre": "Ana", "edad": 20, "calificacion": 95},
    {"nombre": "Luis", "edad": 22, "calificacion": 85},
    {"nombre": "María", "edad": 21, "calificacion": 90},
    {"nombre": "Pedro", "edad": 23, "calificacion": 88}
]

destacados = filtrar_estudiantes(estudiantes)
print(destacados)


#19. Crea una función lambda que filtre los números impares de una lista dada.

filtrar_impares = lambda lista: list(filter(lambda x: x % 2 != 0, lista))

numeros = [1, 2, 3, 4, 5, 6]
resultado = filtrar_impares(numeros)
print(resultado)


#20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()

def filtrar_enteros(lista: list) -> list:
    return list(filter(lambda x: isinstance(x, int), lista))

datos = [1, "hola", 3, "mundo", 5, "7"]
resultado = filtrar_enteros(datos)
print(resultado)


#21. Crea una función que calcule el cubo de un número dado mediante una función lambda

cubo = lambda x: x ** 3

resultado = cubo(4)
print(resultado)


#22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() .

from functools import reduce

def producto_total(lista: list) -> int:
    return reduce(lambda x, y: x * y, lista)

numeros = [2, 3, 4]
resultado = producto_total(numeros)
print(resultado)


#23. Concatena una lista de palabras.Usa la función reduce() .

from functools import reduce

def concatenar_palabras(palabras: list) -> str:
    return reduce(lambda x, y: x + y, palabras)

lista = ["Hola", " ", "mundo", "!"]
resultado = concatenar_palabras(lista)
print(resultado)


#24. Calcula la diferencia total en los valores de una lista. Usa la función reduce() .

from functools import reduce

def diferencia_total(lista: list) -> int:
    return reduce(lambda x, y: x - y, lista)

numeros = [20, 5, 3]
resultado = diferencia_total(numeros)
print(resultado)


#25. Crea una función que cuente el número de caracteres en una cadena de texto dada.

def contar_caracteres(texto: str) -> int:
    return len(texto)

cadena = "Hola, mundo"
resultado = contar_caracteres(cadena)
print(resultado)


#26. Crea una función lambda que calcule el resto de la división entre dos números dados.

resto = lambda x, y: x % y

resultado = resto(10, 3)
print(resultado)


#27. Crea una función que calcule el promedio de una lista de números.

def promedio(lista: list) -> float:
    return sum(lista) / len(lista) if lista else 0

numeros = [4, 8, 15, 16, 23, 42]
resultado = promedio(numeros)
print(resultado)


#28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

def primer_duplicado(lista: list):
    vistos = set()
    for elem in lista:
        if elem in vistos:
            return elem
        vistos.add(elem)
    return None

lista = [3, 5, 1, 4, 5, 2, 3]
resultado = primer_duplicado(lista)
print(resultado)


#29. Crea una función que convierta una variable en una cadena de texto y 
# enmascare todos los caracteres  con el carácter '#', excepto los últimos cuatro.

def enmascarar_variable(valor) -> str:
    texto = str(valor)
    if len(texto) <= 4:
        return texto
    return '#' * (len(texto) - 4) + texto[-4:]

print(enmascarar_variable(123456789))   
print(enmascarar_variable("contraseña")) 


#30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras 
# pero en diferente orden.

def son_anagramas(palabra1: str, palabra2: str) -> bool:
    return sorted(palabra1.lower()) == sorted(palabra2.lower())

print(son_anagramas("amor", "roma"))  
print(son_anagramas("perro", "ropa"))  


#31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. 
# Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.

class NombreNoEncontradoError(Exception):
    pass

def buscar_nombre_en_lista():
    nombres = input("Introduce una lista de nombres separados por comas: ").split(",")
    nombres = [nombre.strip() for nombre in nombres]
    nombre_buscar = input("Introduce el nombre a buscar: ").strip()
    
    if nombre_buscar in nombres:
        print(f"El nombre '{nombre_buscar}' fue encontrado.")
    else:
        raise NombreNoEncontradoError(f"El nombre '{nombre_buscar}' no está en la lista.")

try:
    buscar_nombre_en_lista()
except NombreNoEncontradoError as e:
    print(e)


#32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y 
# devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.

def obtener_puesto(nombre_completo: str, empleados: list) -> str:
    for empleado in empleados:
        if empleado.get("nombre") == nombre_completo:
            return empleado.get("puesto", "Puesto no especificado")
    return "La persona no trabaja aquí."

empleados = [
    {"nombre": "Ana Pérez", "puesto": "Gerente"},
    {"nombre": "Luis Gómez", "puesto": "Contador"},
    {"nombre": "Marta Ruiz", "puesto": "Secretaria"}
]

print(obtener_puesto("Luis Gómez", empleados))    
print(obtener_puesto("Carlos Sánchez", empleados))  


#33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

sumar_listas = lambda lista1, lista2: list(map(lambda x, y: x + y, lista1, lista2))

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
resultado = sumar_listas(lista_a, lista_b)
print(resultado) 


#34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. 
# Los métodos disponibles son: crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . 
# El objetivo es implementar estos métodos para manipular la estructura del árbol. 
# Código a seguir: 1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas. 
# 2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad. 
# 3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas. 
# 4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes. 
# 5. Implementar el método quitar_rama para eliminar una rama en una posición específica.

class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        self.ramas = [rama + 1 for rama in self.ramas]

    def quitar_rama(self, posicion):
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)
        else:
            raise IndexError("Posición de rama inválida")

    def info_arbol(self):
        return (
            f"Longitud del tronco: {self.tronco}\n"
            f"Número de ramas: {len(self.ramas)}\n"
            f"Longitudes de las ramas: {self.ramas}"
        )

# Caso de uso

arbol = Arbol()          # 1. Crear un árbol
arbol.crecer_tronco()    # 2. Crecer el tronco una unidad
arbol.nueva_rama()       # 3. Añadir una nueva rama
arbol.crecer_ramas()     # 4. Crecer todas las ramas una unidad
arbol.nueva_rama()       # 5. Añadir otra nueva rama
arbol.nueva_rama()       # 5. Añadir otra nueva rama más
arbol.quitar_rama(2)     # 6. Retirar la rama en posición 2 (tercera rama)
print(arbol.info_arbol()) # 7. Información del árbol


#36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. 
# Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo. 
# Código a seguir: Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante true y false
# Implementar el método retirar_dinero para retirar dinero del saldo del usuario. 
# Lanzará un error en caso de no poder hacerse. Implementar el método transferir_dinero para realizar una transferencia 
# desde otro usuario al usuario actual. Lanzará un error en caso de no poder hacerse.
# Implementar el método agregar_dinero para agregar dinero al saldo del usuario. 
# Caso de uso: 
#Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
#Agregar 20 unidades de saldo de "Bob". Hacer una transferencia de 80 unidades desde "Bob" a "Alicia". 
#Retirar 50 unidades de saldo a "Alicia".

class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser positiva.")
        if cantidad > self.saldo:
            raise ValueError(f"{self.nombre} no tiene saldo suficiente para retirar {cantidad}.")
        self.saldo -= cantidad

    def transferir_dinero(self, usuario_origen, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a transferir debe ser positiva.")
        if not usuario_origen.cuenta_corriente:
            raise ValueError(f"{usuario_origen.nombre} no tiene cuenta corriente para transferir dinero.")
        if cantidad > usuario_origen.saldo:
            raise ValueError(f"{usuario_origen.nombre} no tiene saldo suficiente para transferir {cantidad}.")
        usuario_origen.saldo -= cantidad
        self.saldo += cantidad

    def agregar_dinero(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a agregar debe ser positiva.")
        self.saldo += cantidad


# Caso de uso corregido
alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)

bob.agregar_dinero(40)         
alicia.transferir_dinero(bob, 80)  
alicia.retirar_dinero(50)       

print(f"Saldo Alicia: {alicia.saldo}")  
print(f"Saldo Bob: {bob.saldo}")


#37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: 
# reemplazar_palabras , procesar_texto . contar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que 
# definir primero y llamar dentro de la función Código a seguir: Crear una función contar_palabras para contar el número de veces 
# que aparece cada palabra en el texto. Tiene que devolver un diccionario. 
# Crear una función reemplazar_palabras para remplazar una que devolver el texto con el remplazo de palabras. 
# Crear una función palabra_original del texto por una palabra_nueva . Tiene eliminar_palabra para eliminar una palabra del texto. 
# Tiene que devolver el texto con la palabra eliminada. Crear la función procesar_texto que tome un texto, 
# una opción(entre "contar", "reemplazar", "eliminar") y un número de argumentos variable según la opción indicada. 
# Caso de uso: Comprueba el funcionamiento completo de la función procesar_texto

def contar_palabras(texto):
    palabras = texto.lower().split()
    frecuencias = {}
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    return frecuencias

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)

def eliminar_palabra(texto, palabra_a_eliminar):
    palabras = texto.split()
    palabras_filtradas = [p for p in palabras if p != palabra_a_eliminar]
    return ' '.join(palabras_filtradas)

def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        if len(args) != 2:
            raise ValueError("Para 'reemplazar' se requieren dos argumentos: palabra_original, palabra_nueva")
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        if len(args) != 1:
            raise ValueError("Para 'eliminar' se requiere un argumento: palabra_a_eliminar")
        return eliminar_palabra(texto, args[0])
    else:
        raise ValueError(f"Opción desconocida: {opcion}")

# Caso de uso
texto_ejemplo = "hola mundo hola universo mundo"

print("Contar palabras:")
print(procesar_texto(texto_ejemplo, "contar"))

print("\nReemplazar 'mundo' por 'planeta':")
print(procesar_texto(texto_ejemplo, "reemplazar", "mundo", "planeta"))

print("\nEliminar 'hola':")
print(procesar_texto(texto_ejemplo, "eliminar", "hola"))


#38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.

def determinar_momento(hora, minuto):
    total_minutos = hora * 60 + minuto

    if 0 <= total_minutos < 6 * 60:
        return "Noche"
    elif 6 * 60 <= total_minutos < 12 * 60:
        return "Día"
    elif 12 * 60 <= total_minutos < 21 * 60:
        return "Tarde"
    elif 21 * 60 <= total_minutos < 24 * 60:
        return "Noche"
    else:
        return "Hora no válida"

def main():
    try:
        hora = int(input("Introduce la hora (0-23): "))
        minuto = int(input("Introduce los minutos (0-59): "))
        if not (0 <= hora <= 23):
            print("La hora debe estar entre 0 y 23.")
            return
        if not (0 <= minuto <= 59):
            print("Los minutos deben estar entre 0 y 59.")
            return
        momento = determinar_momento(hora, minuto)
        print(f"Son las {hora:02d}:{minuto:02d} y es {momento}.")
    except ValueError:
        print("Por favor, introduce números enteros válidos para hora y minutos.")

if __name__ == "__main__":
    main()


#39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica. 
# Las reglas de calificación son: 
# -0 -69 insuficiente 
#-70-79 bien
#-80 -89 muy bien 
#-90 -100 excelente

def obtener_calificacion_texto(nota):
    if 0 <= nota <= 69:
        return "Insuficiente"
    elif 70 <= nota <= 79:
        return "Bien"
    elif 80 <= nota <= 89:
        return "Muy bien"
    elif 90 <= nota <= 100:
        return "Excelente"
    else:
        return "Calificación inválida"

def main():
    try:
        nota = int(input("Introduce la calificación (0-100): "))
        resultado = obtener_calificacion_texto(nota)
        print(f"La calificación es: {resultado}")
    except ValueError:
        print("Por favor, introduce un número entero válido.")

if __name__ == "__main__":
    main()


#40.Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o "triangulo" ) 
# y datos (una tupla con los datos necesarios para calcular el área de la figura).

import math

def calcular_area(figura, datos):
    if figura == "triangulo":
        base, altura = datos
        return (base * altura) / 2
    elif figura == "rectangulo":
        ancho, alto = datos
        return ancho * alto
    elif figura == "circulo":
        (radio,) = datos
        return math.pi * radio ** 2
    else:
        raise ValueError("Figura no reconocida")

# Ejemplo de uso:
print(calcular_area("triangulo", (3, 4)))   
print(calcular_area("rectangulo", (5, 6))) 
print(calcular_area("circulo", (2,)))


#41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el monto final 
# de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo siguiente: 
# 1. Solicita al usuario que ingrese el precio original de un artículo. 
# 2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no). 
# 3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento. 
# 4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor a cero). 
# Por ejemplo, descuento de 15€. 
# 5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él. 
# 6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu programa de Python.

def calcular_precio_final():
    precio_original = float(input("Ingresa el precio original del artículo: "))
    tiene_cupon = input("¿Tienes un cupón de descuento? (sí/no): ").strip().lower()

    if tiene_cupon == "sí" or tiene_cupon == "si":
        valor_cupon = float(input("Ingresa el valor del cupón de descuento: "))
        if valor_cupon > 0:
            precio_final = precio_original - valor_cupon
            if precio_final < 0:
                precio_final = 0  # Precio no puede ser negativo
            print(f"El precio final con descuento es: {precio_final}€")
        else:
            print("Valor de cupón inválido. No se aplicó descuento.")
            print(f"El precio final es: {precio_original}€")
    elif tiene_cupon == "no":
        print(f"El precio final es: {precio_original}€")
    else:
        print("Respuesta no válida. No se aplicó descuento.")
        print(f"El precio final es: {precio_original}€")

calcular_precio_final()