
class Paciente:
    def __init__(self,nombre,prioridad):
        self.nombre= nombre
        self.prioridad=prioridad
    
    
class Cola:
    def __init__(self):
        self.items=[]

    def encolar(self,dato):
        self.items.append(dato)

    def desencolar(self):
        try:
            return self.items.pop(0)
        except IndexError:
            raise ValueError("La cola esta vacia")

    def colaVacia(self):
        return self.items == []

        
def atenderPaciente(cola):
    colaP1=Cola()
    colaP2=Cola()
    colaP3=Cola()

    #print cola.desencolar().prioridad
    while cola.colaVacia() != True:
        #print cola.desencolar().prioridad
        paciente=cola.desencolar()
        if paciente.prioridad==1:
            #print "Encolado P1"
            colaP1.encolar(paciente)
        elif paciente.prioridad==2:
            #print "Encolado P2"
            colaP2.encolar(paciente)
        else:
            #print "Encolado P3"
            colaP3.encolar(paciente)

    print "COLA PRIORIDAD 1:"
    while colaP1.colaVacia()!= True:
        print colaP1.desencolar().nombre
    print "COLA PRIORIDAD 2"
    while colaP2.colaVacia()!= True:
        print colaP2.desencolar().nombre
    print "COLA PRIORIDAD 3"
    while colaP3.colaVacia()!= True:
        print colaP3.desencolar().nombre              
    
            

col=Cola()
paciente=Paciente("Daniel",2)
col.encolar(paciente)
paciente=Paciente("Alejandro",2)
col.encolar(paciente)
paciente=Paciente("Toro",1)
col.encolar(paciente)
paciente=Paciente("Tobar",3)
col.encolar(paciente)
paciente=Paciente("Juan",1)
col.encolar(paciente)
paciente=Paciente("Pablo",2)
col.encolar(paciente)
paciente=Paciente("Avila",3)
col.encolar(paciente)
paciente=Paciente("Diaz",1)
col.encolar(paciente)
paciente=Paciente("David",2)
col.encolar(paciente)
paciente=Paciente("Stevens",3)
col.encolar(paciente)

#print col.desencolar().prioridad
atenderPaciente(col)


