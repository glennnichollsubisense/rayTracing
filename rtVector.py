from math import sqrt
import matrices as mx



class rtVector(mx.rtMatrix):

    def __init__(self, x=0, y=0, z=0):

        self.vectorConstant = 0.0
        self.deltaConstant = 0.00001
        self.unitConstant = 1.0
        self.zeroConstant = 0.0

        super(rtVector, self).__init__(1, 4)
        self.setRow(0, [x, y, z, self.vectorConstant])


    def isAPoint(self):
        return False
    
    def isAVector(self):
        return True

    def isAUnitVector (self):
        return abs (self.magnitudeOfVector() - self.unitConstant) < self.deltaConstant

    def negate (self, vec):
        return self.subtractBFromA (self.newNullVector(), vec)

    def subtractAnotherFromMe (self, another):
    
        if another.isAPoint():
            raise badSubtraction ('Cannot subtract a point from a vector')

        return self.subtractFromMe(another)

    def multiplyByScalar (self, scalar):    
        return super(rtVector, self).multiplyByScalar(scalar)
    
    
    def divideByScalar (self, scalar):
        return super(rtVector, self).divideByScalar(scalar)
    
    
    def magnitude (self):
        
        return sqrt((self.getValue(0, 0) * self.getValue(0, 0)) + \
                    (self.getValue(0, 1) * self.getValue(0, 1)) + \
                    (self.getValue(0, 2) * self.getValue(0, 2))
        )
    
    def normalise (self):
    
        magnitude = self.magnitude()
    
        if abs(magnitude - self.zeroConstant) < self.deltaConstant:
            raise badNormalise ('normalise cannot work on a null vector')

        #print ('about to divide by scalar')
        res = self.divideByScalar(magnitude)
        #print ('got res ')
        #res.showMe()
        return res.matrix['data']
    
    
    def dotProductWithAnother (self, another):
    
        if not another.isAVector():
            raise badDotProduct ('dot product only works on vectors')

        return      (self.getValue(0, 0) * another.getValue(0, 0)) + \
                    (self.getValue(0, 1) * another.getValue(0, 1)) + \
                    (self.getValue(0, 2) * another.getValue(0, 2)) + \
                    (self.getValue(0, 3) * another.getValue(0, 3))
    
    
    def crossProductWithAnother (self, another):
    
        if not another.isAVector():
            raise badCrossProduct ('dot product only works on vectors')

        resMatrix = mx.rtMatrix(1, 4)

        resMatrix.setValue (0, 0, (self.getValue(0, 1) * another.getValue(0, 2)) - (self.getValue(0, 2) * another.getValue(0, 1)))
        resMatrix.setValue (0, 1, (self.getValue(0, 2) * another.getValue(0, 0)) - (self.getValue(0, 0) * another.getValue(0, 2)))
        resMatrix.setValue (0, 2, (self.getValue(0, 0) * another.getValue(0, 1)) - (self.getValue(0, 1) * another.getValue(0, 0)))
        resMatrix.setValue (0, 3, self.vectorConstant)
        return resMatrix.matrix['data']
    

    # Exceptions
    class badSubtraction(Exception):    
        def __init__(self, message):
            super(badSubtraction, self).__init__(message)
    
    class badNormalise(Exception):    
        def __init__(self, message):
            super(badNormalise, self).__init__(message)
            
    class badDotProduct(Exception):
        def __init__(self, message):
            super(badDotProduct, self).__init__(message)
            
    class badCrossProduct(Exception):
        def __init__(self, message):
            super(badCrossProduct, self).__init__(message)
            
