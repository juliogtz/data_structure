# Author: Julio Gtz.
# Data Structure list [0, 1, 2, 3, 4, 5 [1, 2, 3], (2, 3 , 5,), "Hello"]
# Comments: Try to understand how to use and implement the list in python.

def simple_list(list):
    return list


def functions_list(list):
    print "---- append(x) Agrega un item al final de la lista. ----"
    list.append("add_append")
    list[len(list):] = ["add_append_2"]

    print "---- extend(L) Extiende la lista agregandole todos los items de la lista dada. Equivale a a[len(a):] = L. ----"
    list.extend(['A', 'B', 'C'])

    print "---- insert(i, x) Inserta un item en una posicion dada. El primer argumento es el indice del item delante del cual se insertara, por lo tanto a.insert(0, x)"
    list.insert(0,"insert_0")

    print "---- remove(x) Quita el primer item de la lista cuyo valor sea x. Es un error si no existe tal item."
    list.remove("insert_0")

    print "--- pop([i]) ---- Quita el item en la posicion dada de la lista, y lo devuelve. Si no se especifica un indice, a.pop() quita y devuelve el ultimo item de la lista. (Los corchetes que encierran a i en la firma del metodo denotan que el parametro es opcional, no que deberias escribir corchetes en esa posicion. Veras esta notacion con frecuencia en la Referencia de la Biblioteca de Python.)"
    list.pop(3)

    print "--- clear() Quita todos los elementos de la lista. Equivalente a del list[:] list = []"
    #list=[]
    print "El index del valor 'add_append' " + str(list.index('add_append'))
    print "---- count(x) "
    print "Devuelve el numero de veces que x aparece en la lista: " + str(list.count("add_append"))
    print "lista ordenada: "+ str(sorted(list))
    print "Crear un reverse en la lista - o voltear los elementos de la lista: "
    list.reverse()
    return list


def pila(list):
    print "Una pila es una estructura de datos secuencial en la que el ultimo elemento" \
          "insertado es el primero en retirarse (LIFO) Last in, first out y " \
          "puede implementarse directamente con los metodos append y pop."

    # agrega un valor al finala de la lista.
    list.append(20)

    # quita el ultimo elemento de la lista.
    list.pop()

    return list





# define list
list = [1 , 2, 3, [1, 2, [1, 2, 4], {"name":"Julio"}, ], 9 ]


# simple_list(list)
print pila(list)




