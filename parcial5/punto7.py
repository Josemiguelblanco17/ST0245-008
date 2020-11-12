pila=[]
pila1=[]
pila.append(1)
pila.append(2)
pila.append(3)
pila.append(4)
pila.append(5)
print(pila)
while(len(pila)!=0):
    pila1.append(pila.pop())
    print(pila1)

print(pila) #pila 1 esta vacia