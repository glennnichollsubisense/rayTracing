from math import sqrt
import matrices as mx

class rtPoint(mx.rtMatrix):

    def __init__(self, x=0, y=0, z=0):

        self.pointConstant = 1.0
        self.deltaConstant = 0.00001
        self.unitConstant = 1.0
        self.zeroConstant = 0.0

        super(rtPoint, self).__init__(1, 4)
        self.setRow(0, [x, y, z, self.pointConstant])

        
    def isAPoint(self):
        return True
    
    def isAVector(self):
        return False
    
    def addWithAnother(self, another):
    
        if another.isAPoint():
            raise (badAddition('Cannot add two points'))

        return super(rtPoint, self).addWithAnother(another)

    
    def subtractAnotherFromMe (self, another):
        return super(rtPoint, self).subtractFromMe(another)
    
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
    
