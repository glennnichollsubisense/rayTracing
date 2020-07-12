from colours import rtColour
from rtColourFactory import rtColourFactory

class rtMaterial(object):

    def __init__(self, pColour=None, pDiffuse=None, pSpecular=None, pShininess=None, pAmbient=None):


        self.sColour = pColour

        self.sDiffuse = 0.9
        if pDiffuse != None:
            self.sDiffuse = pDiffuse
        self.sAmbient = 0.1
        if pAmbient != None:
            self.sAmbient = pAmbient
        self.sSpecular = 0.9
        if pSpecular != None:
            self.sSpecular = pSpecular
        self.sShininess = 200
        if pShininess != None:
            self.sShininess = pShininess
            
        
    def setColour(self, colour):
        self.sColour = colour
            
    def getColour(self):
        return self.sColour
        
    def getAmbient(self):
        return self.sAmbient
    
    def getDiffuse(self):
        return self.sDiffuse
        
    def getSpecular(self):
        return self.sSpecular
    
    def getShininess(self):
        return self.sShininess

    def setDefaultValues(self):

        rtf = rtColourFactory()
        self.sColour = rtf.newWhite()
        self.sDiffuse = 0.9
        self.sAmbient = 0.1
        self.sSpecular = 0.9
        self.sShininess = 200
    
    def setGrassValues(self):

        rtf = rtColourFactory()
        self.sColour = rtf.newGreen()
        self.sDiffuse = 0.8
        self.sAmbient = 0.5
        self.sSpecular = 0.2
        self.sShininess = 50
    
    def setTextBookGreen(self):

        rtf = rtColourFactory()
        self.sColour = rtColour(1.0, 0.2, 1.0)
        self.sDiffuse = 0.9
        self.sAmbient = 0.1
        self.sSpecular = 0.9
        self.sShininess = 200
    
