class Pelicula:
    def __init__(self,nombre,actor):
        self.nombre= nombre
        self.actor=actor
    
    
class Pila:
    def __init__(self):
        self.items=[]

    def apilar(self,dato):
        self.items.append(dato)

    def desapilar(self):
        return self.items.pop()

    def pilaVacia(self):
        return self.items == []


def buscarPelicula(pila,nomPeli):
    auxPel=Pelicula("","")
    while not pila.pilaVacia():
        auxPel=pila.desapilar()
        if (auxPel.nombre==nomPeli):
            print auxPel.nombre
        
def buscarActor(pila,actorPeli):
    auxPel=Pelicula("","")
    auxPila=Pila()
    while not pila.pilaVacia():
        auxPel=pila.desapilar()
        if (auxPel.actor==actorPeli):
            auxPila.apilar(auxPel)
    while not auxPila.pilaVacia():
        print auxPila.desapilar().nombre
            

pila1=Pila()
peli=Pelicula("La gran estafa","Brad Pitt")
pila1.apilar(peli)
peli=Pelicula("El club de la pelea","Brad Pitt")
pila1.apilar(peli)
peli=Pelicula("Iron Man","Robert Downey")
pila1.apilar(peli)
