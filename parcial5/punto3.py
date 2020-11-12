#josemiguelblanco
#definir clase nodo
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#definir el constructor del arbol
def build(inorden, preorder, instrt, inend):
    if instrt > inend:
        return None
    tNode = Node(preorder[build.preIndex])
    build.preIndex += 1
    if instrt == inend:
        return tNode
    inindex = arrays(inorden, instrt, inend, tNode.data)
    tNode.left = build(inorden, preorder, instrt, inindex - 1)
    tNode.right = build(inorden, preorder, inindex + 1, inend)
    return tNode

#def la funcion que crea los array
def arrays(array, start, end, data):
    for i in range(start, end + 1):
        if array[i] == data:
            return i

#definimos para cuando esta en postorden
def postorder(a):
    if a is None:
        return None
    else:
        postorder(a.left)
        postorder(a.right)
        print(a.data, end=' ')

#definimos para cuando esta en inorden
def inorden(a):
    if a is None:
        return None
    else:
        inorden(a.left)
        print(a.data, end=' ')
        inorden(a.right)

inordenado = ['I', 'A', 'B', 'E', 'G', 'L', 'D', 'C', 'F', 'M', 'K', 'H', 'J']
def preorden(a):
    if a is None:
        return None
    else:
        print(a.data, end=' ')
        preorden(a.left)
        preorden(a.right)


preordenado = ['G', 'E', 'A', 'I', 'B', 'M', 'C', 'L', 'D', 'F', 'K', 'J', 'H']


build.preIndex = 0
arbol = build(inordenado, preordenado, 0, len(inordenado) - 1)
inorden(arbol)  #arbol en inorden
print(" ")
preorden(arbol) #arbol construido en preorden
print(" ")