class Cauchonegro:
  
    def __init__(self,  velocidad,  control,  desc,  machetazo):
        self.velocidad= velocidad
        self.control= control
        self.desc= desc
        self.achetazo=machetazo
    
    def getVelocidad(self):
        return self.velocidad
    
    def getControl(self):
        return self.control
    
    def getDesc(self):
        return self.desc
    

    def setVelocidad(self, velocidad):
        self.velocidad = velocidad
    
    def setControl(self, control):
        self.control = control
    
    def setDesc(self, desc):
        self.desc = desc
    
