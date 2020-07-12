from math import sqrt
import matrices as mx



class rtVector(object):

    def __init__(self, x=0, y=0, z=0):

        self.vectorConstant = 0.0
        self.deltaConstant = 0.00001
        self.unitConstant = 1.0
        self.zeroConstant = 0.0

        self.matrix = mx.rtMatrix(1, 4)
        self.matrix.setRow(0, [x, y, z, self.vectorConstant])


    def isAPoint(self):
        return False
    
    def isAVector(self):
        return True

    def isAUnitVector (self):
        return abs (self.magnitudeOfVector() - self.unitConstant) < self.deltaConstant

    def negate (self):
        return rtVector().subtractAnotherFromMe (self)

    def getMatrixData(self):
        return self.matrix.matrix['data']

    def generalTransform (self, mtTransform):
        newVector = rtVector()
        newVector.matrix = mtTransform.transform (self.matrix.transpose())
        newVector.matrix = newVector.matrix.transpose()
        return newVector

    def scale (self, mtScaling):
        return self.generalTransform(mtScaling)


    def addWithAnother (self, another):

        newVector = rtVector()
        newVector.matrix = self.matrix.addWithAnother(another.matrix)
        return newVector

    def equalToAnother (self, another):

        myData = self.getMatrixData()
        anotherData = another.getMatrixData()
        
        areSame = True
        if abs(myData[0][0]) - abs(anotherData[0][0]) > self.deltaConstant:
            areSame = False
        if abs(myData[0][1]) - abs(anotherData[0][1]) > self.deltaConstant:
            areSame = False
        if abs(myData[0][2]) - abs(anotherData[0][2]) > self.deltaConstant:
            areSame = False

        return areSame

        
    def subtractAnotherFromMe (self, another):
    
        if another.isAPoint():
            raise badSubtraction ('Cannot subtract a point from a vector')

        tMatrix = self.matrix.subtractFromMe(another.matrix)
        tVec = rtVector()
        tVec.matrix = tMatrix
        
        return tVec

    def multiplyByScalar (self, scalar):

        newVector = rtVector()
        newVector.matrix = self.matrix.multiplyByScalar(scalar)
        return newVector

    
    def divideByScalar (self, scalar):

        newVector = rtVector()
        newVector.matrix = self.matrix.divideByScalar(scalar)
        return newVector
    
    
    def magnitude (self):
        
        return sqrt((self.matrix.getValue(0, 0) * self.matrix.getValue(0, 0)) + \
                    (self.matrix.getValue(0, 1) * self.matrix.getValue(0, 1)) + \
                    (self.matrix.getValue(0, 2) * self.matrix.getValue(0, 2))
        )
    
    def normalise (self):
    
        magnitude = self.magnitude()
    
        if abs(magnitude - self.zeroConstant) < self.deltaConstant:
            raise badNormalise ('normalise cannot work on a null vector')

        res = self.divideByScalar(magnitude)
        tdata = res.getMatrixData() 
        resVector = rtVector(tdata[0][0], tdata[0][1], tdata[0][2])
        return resVector
    
    
    def dotProductWithAnother (self, another):
    
        if not another.isAVector():
            raise badDotProduct ('dot product only works on vectors')

        return      (self.matrix.getValue(0, 0) * another.matrix.getValue(0, 0)) + \
                    (self.matrix.getValue(0, 1) * another.matrix.getValue(0, 1)) + \
                    (self.matrix.getValue(0, 2) * another.matrix.getValue(0, 2)) + \
                    (self.matrix.getValue(0, 3) * another.matrix.getValue(0, 3))
    
    
    def crossProductWithAnother (self, another):
    
        if not another.isAVector():
            raise badCrossProduct ('dot product only works on vectors')

        resMatrix = mx.rtMatrix(1, 4)

        resMatrix.setValue (0, 0, (self.matrix.getValue(0, 1) * another.matrix.getValue(0, 2)) - (self.matrix.getValue(0, 2) * another.matrix.getValue(0, 1)))
        resMatrix.setValue (0, 1, (self.matrix.getValue(0, 2) * another.matrix.getValue(0, 0)) - (self.matrix.getValue(0, 0) * another.matrix.getValue(0, 2)))
        resMatrix.setValue (0, 2, (self.matrix.getValue(0, 0) * another.matrix.getValue(0, 1)) - (self.matrix.getValue(0, 1) * another.matrix.getValue(0, 0)))
        resMatrix.setValue (0, 3, self.vectorConstant)
        return resMatrix.matrix['data']
    

    def reflectWithAnother(self, another):

        dotMatrix = self.dotProductWithAnother(another)
        resVector = rtVector()
        tMatrix1 = another.matrix.multiplyByScalar(2).multiplyByScalar(dotMatrix)
        tMatrix2 = self.matrix.subtractFromMe(tMatrix1)
        resVector.matrix = tMatrix2
        return resVector
        

    def showMe(self, label=''):
        print ('%s *** Vector ***' % label) 
        print ('%s : %s : %s' % (self.matrix.getValue(0,0), self.matrix.getValue(0, 1), self.matrix.getValue(0, 2)))

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
            
