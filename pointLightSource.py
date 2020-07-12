import colours
from rtColourFactory import rtColourFactory
import rtPoint


class PointLightSource(object):

    def __init__(self, pColour=None, pPoint=None):


        rtf = rtColourFactory()
        self.sColour = rtf.newWhite()
        if pColour != None:
            self.sColour = pColour
            
        self.sPoint = rtPoint.rtPoint()
        if pPoint != None:
            self.sPoint = pPoint
            
        
    def setColour(self, colour):
        self.sColour = colour
        
    def setPoint(self, point):
        self.sPoint = point
    
    def getColour(self):
        return self.sColour
        
    def getPoint(self):
        return self.sPoint
    
    
