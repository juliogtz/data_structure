class Stack:

    def __init__(self):
        self.stack = []
        self.aux_stack = []
        print "Guardamos el stack"

    def size(self):
        return len(self.stack)

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        self.stack.pop()

    def tos(self):
        return self.stack[len(self.stack)-1]

    def empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def clear(self):
        self.stack = []



# Ejemplo de uso de clase

# Creamos una pila ( stack )
stackobj = Stack()

# Insertamos un elemento
stackobj.push(7)

# Insertamos segundo elemento
stackobj.push(9)

# Verificamos el size del stack
stackobj.size()

# Borramos un elemento
stackobj.pop()

# Obtenemos el ultimo elemento
stackobj.tos()

# Verificamos si esta vacia el stack
stackobj.empty()

# Limpiamos el stack
stackobj.clear()


# 1.- Ejemplo
# Intercambiar la pila de atras hacia delante. (Reverse), sabiendo las reglas de una pila (stack)


stackobj2 = Stack()
# Iniciarlizar el stack

for n in range(0, 10):
    print n
    stackobj2.push(n)

print " ------ "

# Almacenar Stack Auxiliar

for n in range(stackobj2.size(), 0, -1):
    print stackobj2.stack[n-1]
    stackobj2.aux_stack.append(stackobj2.stack[n-1])


# Limpiar pila

for n in range(0, stackobj2.size()):
    stackobj2.pop()

print " ------ "

# Ordenar pila en reverse

for n in range(0, len(stackobj2.aux_stack)):
    stackobj2.push(stackobj2.aux_stack[n])
    print stackobj2.aux_stack[n]


print(stackobj2.stack)


