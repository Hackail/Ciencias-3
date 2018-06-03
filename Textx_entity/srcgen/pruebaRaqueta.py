class Raqueta:
  
    def __init__(self,  velocidad,  control,  cauchoNegro,  desc,  cauchoRojo,  machetazo):
        self.velocidad= velocidad
        self.control= control
        self.cauchoNegro= cauchoNegro
        self.desc= desc
        self.cauchoRojo= cauchoRojo
        self.achetazo=machetazo
    
    def getVelocidad(self):
        return self.velocidad
    
    def getControl(self):
        return self.control
    
    def getCauchonegro(self):
        return self.cauchoNegro
    
    def getDesc(self):
        return self.desc
    
    def getCauchorojo(self):
        return self.cauchoRojo
    

    def setVelocidad(self, velocidad):
        self.velocidad = velocidad
    
    def setControl(self, control):
        self.control = control
    
    def setCauchonegro(self, cauchoNegro):
        self.cauchoNegro = cauchoNegro
    
    def setDesc(self, desc):
        self.desc = desc
    
    def setCauchorojo(self, cauchoRojo):
        self.cauchoRojo = cauchoRojo
    
