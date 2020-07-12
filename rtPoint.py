from math import sqrt
import matrices as mx
from rtVector import rtVector

class rtPoint(object):

    def __init__(self, x=0, y=0, z=0):

        self.pointConstant = 1.0
        self.deltaConstant = 0.00001
        self.unitConstant = 1.0
        self.zeroConstant = 0.0

        self.matrix = mx.rtMatrix(1, 4)
        self.matrix.setRow(0, [x, y, z, self.pointConstant])

        
    def isAPoint(self):
        return True
    
    def isAVector(self):

        # GNGN put this onto the superclass
        return False
    

    def getMatrixData(self):
        return self.matrix.matrix['data']

    def setFromMatrix(self, another):

        self.matrix.setRow (0, [another[0], another[1], another[2], self.pointConstant])

        
    def setFromAnother(self, another):

        self.matrix.setRow (0, [another.matrix.getValue(0, 0), another.matrix.getValue(0, 1), another.matrix.getValue(0, 2), self.pointConstant])

        
    def addWithAnother(self, another):
    
        if another.isAPoint():
            raise (badAddition('Cannot add two points'))

        newPoint = rtPoint()
        newPoint.matrix = self.matrix.addWithAnother(another.matrix)
        return newPoint
    
    
    def subtractAnotherFromMe (self, another):

        newVector = rtVector()
        newVector.matrix = self.matrix.subtractFromMe(another.matrix)
        return newVector
    
    def multiplyByScalar (self, scalar):    
        raise badScalarMultiplication ('cannot multiply a point by a scalar')
    
    
    def divideByScalar (self, scalar):    
        raise badScalarDivision ('cannot divide a point by a scalar')
        
    
    def magnitude (self):    
        raise badMagnitude ('cannot get the magnitude of a point')
        
    
    def normalise (self):    
        raise badNormalise ('cannot normalise a point')
        
    
    def dotProductWithAnother (self, another):    
        raise badDotProduct ('dot product doesnt work on points')
    
    
    def crossProductWithAnother (self, another):    
        raise badCrossProduct ('cross product doesnt work on points')


    def generalTransform (self, mtTransform):
        newPoint = rtPoint()
        newPoint.matrix = mtTransform.transform (self.matrix.transpose())
        newPoint.matrix = newPoint.matrix.transpose()
        return newPoint

    def translate (self, mtTranslation):
        return self.generalTransform(mtTranslation)

    def shear (self, mtShear):
        return self.generalTransform(mtShear)

    def rotate (self, mtRotate):
        return self.generalTransform(mtRotate)

    def scale (self, mtScaling):
        return self.generalTransform(mtScaling)

    
    def showMe(self, txtPrefix=''):
        print ('%s *** Point ***' % txtPrefix)
        self.matrix.showMe()
        
## Exceptions
    
class badAddition(Exception):    
    def __init__(self, message):
        super(badAddition, self).__init__(message)

class badScalarMultiplication(Exception):
    def __init__(self, message):
        super(badScalarMultiplication, self).__init__(message)
                
class badScalarDivision(Exception):
    def __init__(self, message):
        super(badScalarDivision, self).__init__(message)
            
class badMagnitude(Exception):
    def __init__(self, message):
        super(badMagnitude, self).__init__(message)
            
class badNormalise(Exception):
    def __init__(self, message):
        super(badNormalise, self).__init__(message)
            
class badDotProduct(Exception):
    def __init__(self, message):
        super(badDotProduct, self).__init__(message)
            
class badCrossProduct(Exception):
    def __init__(self, message):
        super(badCrossProduct, self).__init__(message)
            
    
if __name__== "__main__":
    
    ##  Testing scripts
    pass
    
