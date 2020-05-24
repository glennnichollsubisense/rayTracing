from math import sqrt
import matrices as mx



class PointAndVector(mx.rtMatrix):

    def __init__(self, pointOrVector):

        self.pointConstant = 1.0
        self.vectorConstant = 0.0
        self.deltaConstant = 0.00001
        self.unitConstant = 1.0
        self.zeroConstant = 0.0

        mx.rtMatrix.__init__(self, 1, 4)
        if pointOrVector == 'point':
            self.setValue(0, 3, self.pointConstant)
        else:
            self.setValue(0, 3, self.vectorConstant)
        


    def isAPoint(self):
        return abs(self.pointConstant - self.getValue(0, 3)) < self.deltaConstant

    def isAVector(self):
        return abs(self.vectorConstant - self.getValue(0, 3)) < self.deltaConstant
    
    def newPoint(self, x=0, y=0, z=0):
        bPt = mx.rtMatrix(1, 4)
        bPt.setRow(0, [x, y, z, self.pointConstant])
        return bPt
    
    def newOriginPoint(self):
        return self.newPoint()
    
    def newVector(self, x=0, y=0, z=0):

        bVc = mx.rtMatrix(1, 4)
        bVc.setRow(0, [x, y, z, self.vectorConstant])
        return bVc
    
    def newNullVector(self):
        return self.newVector()
    
    def negateVector (self, vec):
        return self.subtractBFromA (self.newNullVector(), vec)
    
    
    def addWithAnother(self, another):
    
        if self.isAPoint() and another.isAPoint():
            raise (badAddition('Cannot add two points'))

        return super(PointAndVector, self).addWithAnother(another)

    
    def subtractAnotherFromMe (self, another):
    
        if self.isAVector() and another.isAPoint():
            raise badSubtraction ('Cannot subtract a point from a vector')

        return self.subtractFromMe(another)
    
    def multiplyByScalar (self, scalar):
    
        if not (self.isAVector()):
            raise badScalarMultiplication ('multiply by scalar only works on vectors')

        return super().multiplyByScalar(scalar)
    
    
    def divideByScalar (self, scalar):
    
        if not (self.isAVector()):
            raise badScalarDivision ('divide by scalar only works on vectors')
        return super.divideByScalar(scalar)
    
    
    def magnitudeOfVector (self):
    
        if not (self.isAVector()):
            raise badMagnitude ('magnitude only works on vectors')
    

        
        return sqrt((self.getValue(0, 0) * self.getValue(0, 0)) + \
                    (self.getValue(0, 1) * self.getValue(0, 1)) + \
                    (self.getValue(0, 2) * self.getValue(0, 2))
        )
    
    def normaliseVector (self):
    
        if not (self.isAVector()):
            raise badNormalise ('normalise only works on vectors')
    
        magnitude = self.magnitudeOfVector()
    
        if abs(magnitude - self.zeroConstant) < self.deltaConstant:
            raise badNormalise ('normalise cannot work on a null vector')

        self.divideByScalar(magnitude)
    
    
    def isAUnitVector (self):
        return abs (self.magnitudeOfVector() - self.unitConstant) < self.deltaConstant
    
    
    
    def dotProductWithAnother (self, another):
    
        if not self.isAVector() or not another.isAVector():
            raise badDotProduct ('dot product only works on vectors')

        return      (self.getValue(0, 0) * another.getValue(0, 0)) + \
                    (self.getValue(0, 1) * another.getValue(0, 1)) + \
                    (self.getValue(0, 2) * another.getValue(0, 2)) + \
                    (self.getValue(0, 3) * another.getValue(0, 3))
    
    
    def crossProductWithAnother (self, another):
    
        if not self.isAVector() or not another.isAVector():
            raise badCrossProduct ('dot product only works on vectors')

        resMatrix = mx.rtMatrix(1, 4)

        resMatrix.setValue (0, 0, (self.getValue(0, 0) * another.getValue(0, 2)) - (self.getValue(0, 2) * another.getValue(0, 1)))
        resMatrix.setValue (0, 1, (self.getValue(0, 2) * another.getValue(0, 0)) - (self.getValue(0, 0) * another.getValue(0, 2)))
        resMatrix.setValue (0, 2, (self.getValue(0, 0) * another.getValue(0, 1)) - (self.getValue(0, 1) * another.getValue(0, 0)))
        resMatrix.setValue (0, 3, self.vectorConstant)
    
    
    ## Exceptions
    
    class badAddition(Exception):
    
        def __init__(self, message):
            super(badAddition, self).__init__(message)
    
    class badSubtraction(Exception):
    
        def __init__(self, message):
            super(badSubtraction, self).__init__(message)
    
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
    
