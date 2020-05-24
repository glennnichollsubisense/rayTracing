import math

from matrices import rtMatrix

class rtMatrixTransformationFactory():

    def __init__(self):
        self.message = 'rtMatrixFactory'
        

    def newTranslation (self, x, y, z):

        mt = rtMatrix(4, 4, True)

        mt.setValue(0, 3, x)
        mt.setValue(1, 3, y)
        mt.setValue(2, 3, z)
        mt.setValue(3, 3, 1)

        return mt

    def newScaling (self, x, y, z):

        mt = rtMatrix(4, 4, True)
        mt.setValue(0, 0, x)
        mt.setValue(1, 1, y)
        mt.setValue(2, 2, z)
        mt.setValue(3, 3, 1)

        return mt

    def newRotation (self, axis, rotation):

        mt = rtMatrix(4, 4, True)

        if axis == 'X':            
            mt.setValue(0, 0, 1.0)
            mt.setValue(1, 1, math.cos(rotation))
            mt.setValue(1, 2, math.sin(rotation) * -1.0)
            mt.setValue(2, 1, math.sin(rotation))
            mt.setValue(2, 2, math.cos(rotation))
            mt.setValue(3, 3, 1.0)
        elif axis == 'Y':            
            mt.setValue(0, 0, math.cos(rotation))
            mt.setValue(0, 2, math.sin(rotation))
            mt.setValue(1, 1, 1.0)
            mt.setValue(2, 0, math.sin(rotation) * -1.0)
            mt.setValue(2, 2, math.cos(rotation))
            mt.setValue(3, 3, 1.0)
        elif axis == 'Z':            
            mt.setValue(0, 0, math.cos(rotation))
            mt.setValue(0, 1, math.sin(rotation) * -1.0)
            mt.setValue(1, 0, math.sin(rotation))
            mt.setValue(1, 1, math.cos(rotation))
            mt.setValue(2, 2, 1.0)
            mt.setValue(3, 3, 1.0)
        else:
            raise Exception('bad rotation')
        
        return mt

    def newShearing (self, shearComponents):

        mt = rtMatrix(4, 4, True)

        mt.setValue(0, 1, shearComponents[0])
        mt.setValue(0, 2, shearComponents[1])
        mt.setValue(1, 0, shearComponents[2])
        mt.setValue(1, 2, shearComponents[3])
        mt.setValue(2, 0, shearComponents[4])
        mt.setValue(2, 1, shearComponents[5])

        return mt
        
        

    
