from pila import *
from arbol import *

def convertir(lista, pila):
    if lista != []:
        if lista[0] in "+-*/":
            nodo_der = pila.desapilar()
            nodo_izq = pila.desapilar()
            pila.apilar(Nodo(lista[0],nodo_izq,nodo_der))
        else:
            pila.apilar(Nodo(lista[0]))
        return convertir(lista[1:],pila)
            

def evaluar(arbol):
    if arbol.valor == "+":
        return evaluar(arbol.izq) + evaluar(arbol.der)
    if arbol.valor == "-":
        return evaluar(arbol.izq) - evaluar(arbol.der)
    if arbol.valor == "/":
        return evaluar(arbol.izq) / evaluar(arbol.der)
    if arbol.valor == "*":
        return evaluar(arbol.izq) * evaluar(arbol.der)
    return int(arbol.valor)
    
exp = raw_input("ingrese l expresion en posfija 1: ").split(" ")
listax=exp[:-2]
pila = Pila()
convertir(listax, pila)
x=evaluar(pila.desapilar())

print x

exp2 = raw_input("ingrese l expresion en posfija 2: ").split(" ")
listay=exp2[:-2]
print listay
pila1 = Pila()
convertir(listay, pila1)
y=evaluar(pila1.desapilar())

print y

exp3 = raw_input("ingrese l expresion en posfija 3: ").split(" ")
listaz=exp3[:-2]

listaz[0]=str(x)
listaz[1]=str(y)
print listaz

pila2 = Pila()
convertir(listaz, pila2)
z=evaluar(pila2.desapilar())
print z
