
from colours import rtColour

class rtColourFactory():

    def __init__(self):
        self.message = 'rtColourFactory'

    def newBlack(self):
        return rtColour(0.0, 0.0, 0.0, 'Black')
    
    def newWhite(self):
        return rtColour(1.0, 1.0, 1.0, 'White')
    
    def newRed(self):
        return rtColour(1.0, 0.0, 0.0, 'Red')
    
    def newGreen(self):
        return rtColour(0.0, 1.0, 0.0, 'Green')
    
    def newBlue(self):
        return rtColour(0.0, 0.0, 1.0, 'Blue')
    
    def newYellow(self):
        return rtColour(1.0, 1.0, 0.0, 'Yellow')
    
    def newCyan(self):
        return rtColour(0.0, 1.0, 1.0, 'Cyan')
    
    def newMagenta(self):
        return rtColour(1.0, 0.0, 1.0, 'Magenta')
        
