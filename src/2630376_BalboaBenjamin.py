"""
Nombre del estudiante: Benjamin Balboa Acosta
Matrícula: 2630376
Ingeniería en Mecatrónica
Metodología de la Programación
Manejo de Listas y Tuplas


RESUMEN EJECUTIVO

Las listas y las tuplas son estructuras de datos secuenciales fundamentales 
en Python que se utilizan para almacenar colecciones ordenadas de elementos. 
Una lista es una colección mutable, lo que significa que sus elementos pueden 
ser modificados, agregados o eliminados después de su creación, lo que la 
hace ideal para conjuntos de datos dinámicos. Por el contrario, una tupla 
es una colección inmutable, lo que significa que una vez definida, sus 
elementos no pueden ser alterados, proporcionando integridad de datos para 
registros fijos como coordenadas o configuraciones. Este documento cubre 
los problemas prácticos que implementan operaciones de listas y manipulaciones 
de tuplas, algoritmos de búsqueda con ciclos for y validaciones robustas 
sin uso de funciones ni bloques de excepción.

PRINCIPIOS Y BUENAS PRÁCTICAS

- Utilizar listas cuando las colecciones requieran adiciones, eliminaciones u 
  ordenamientos frecuentes.
- Utilizar tuplas para estructuras de datos fijas que deban permanecer inalterables.
- Emplear ciclos for para recorrer elementos, buscar coincidencias y validar 
  datos de manera estructurada y segura.
- Aplicar una rigurosa validación de entradas mediante condiciones explícitas 
  en lugar de bloques de manejo de errores.
- Escribir código limpio y legible siguiendo las convenciones de nomenclatura 
  adecuadas (lower_snake_case para variables).
"""


"""
Problem 1: Shopping list basics (list operations)
Trabaja con una lista de productos (strings) y sus cantidades (enteros). El programa debe:
1) Crear una lista inicial de productos.
2) Permitir agregar un nuevo producto al final.
3) Mostrar la cantidad total de elementos en la lista.
4) Verificar si un producto específico está en la lista (booleano is_in_list).
"""

print("- Problema 1: Lista de Compras Básica -")
initial_items_text = "apple, banana, orange"
new_item = "milk"
search_item = "banana"

if not initial_items_text.strip():
    print("Error: el texto de elementos iniciales está vacío")
else:
    items_list = [item.strip() for item in initial_items_text.split(",")]
    
    if new_item.strip():
        items_list.append(new_item.strip())
    
    total_items = len(items_list)
    found_item = False
    for item in items_list:
        if item == search_item.strip():
            found_item = True
            break
    
    print("Lista de elementos:", items_list)
    print("Total de elementos:", total_items)
    print("Elemento encontrado:", str(found_item).lower())



"""
Problem 2: Points and distances with tuples
Descripción:
Usa tuplas para representar dos puntos en un plano 2D: (x1, y1) y (x2, y2). El programa debe:
1) Crear dos tuplas point_a y point_b a partir de entradas numéricas.
2) Calcular la distancia euclidiana entre ambos puntos.
3) Crear una nueva tupla midpoint con el punto medio entre ellos.

Entradas:
- x1, y1, x2, y2 (float; coordenadas de los puntos).

Salidas:
- "Point A:" (x1, y1)
- "Point B:" (x2, y2)
- "Distance:" <distance>
- "Midpoint:" (mx, my)
"""

print("\n- Problema 2: Puntos y Distancias con Tuplas -")
raw_inputs = ["1.0", "2.0", "4.0", "6.0"]
valid_conversion = True
converted_inputs = []

for val in raw_inputs:
    is_float = True
    dot_count = 0
    clean_val = val.strip()
    
    for char_idx in range(len(clean_val)):
        c = clean_val[char_idx]
        if c == '.':
            dot_count += 1
            if dot_count > 1:
                is_float = False
        elif c == '-' and char_idx == 0:
            continue
        elif not ('0' <= c <= '9'):
            is_float = False
            
    if is_float and len(clean_val) > 0:
        converted_inputs.append(float(clean_val))
    else:
        valid_conversion = False
        break

if not valid_conversion:
    print("Error: entrada numérica inválida")
else:
    x1 = converted_inputs[0]
    y1 = converted_inputs[1]
    x2 = converted_inputs[2]
    y2 = converted_inputs[3]

    point_a = (x1, y1)
    point_b = (x2, y2)
    
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    midpoint = ((x1 + x2) / 2.0, (y1 + y2) / 2.0)
    
    print("Punto A:", point_a)
    print("Punto B:", point_b)
    print("Distancia:", round(distance, 4))
    print("Punto medio:", midpoint)


"""
Conclusiones:
Las listas y las tuplas son muy utiles aunque parezcan similares pueden usarse
en diferentes contextos, las listas son mutables y las tuplas son inmutables
se tiene que ver cual es la mejor para cada caso, las listas son mejores para 
cuando se necesita modificar la coleccion de datos y las tuplas son mejores 
para cuando se necesita que los datos permanezcan constantes. las tuplas al no
poder modificarse no reservan memoria de forma innecesaria mientras que las listas
siempre tienen una memoria reservada para poder modificarse
"""

"""
Referencias:
1) Python Software Foundation. (2026). More on Lists - Python Documentation.
   URL: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
2) Python Software Foundation. (2026). Tuples and Sequences - Python Documentation.
   URL: https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
3) Real Python. Python Lists and Tuples.
   URL: https://realpython.com/python-lists-tuples/
4) Programiz. Python List Methods and Operations.
   URL: https://www.programiz.com/python-programming/list
5) W3Schools. Python Lists Tutorial.
   URL: https://www.w3schools.com/python/python_lists.asp
"""

# Repositorio de GitHub: 