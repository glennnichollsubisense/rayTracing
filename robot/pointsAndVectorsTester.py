import sys
import json

import rtPoint as rtp
import rtVector as rtv

class pointsVectorsTester():

    def __init__(self):
        self.name = 'PointsVectorsTester'


    def runIsPoint(self, xyz):

        aPt = rtp.rtPoint(xyz[0], xyz[1], xyz[2])
        return aPt.isAPoint()


    def runIsVector(self, xyz):

        aVc = rtv.rtVector(xyz[0], xyz[1], xyz[2])
        return aVc.isAVector()


    def addPoints(self, matA, matB):

        entityA = entityB = None
        matA = json.loads(matA)
        matB = json.loads(matB)
        
        entityA = rtp.rtPoint(matA[0], matA[1], matA[2])
        entityB = rtp.rtPoint(matB[0], matB[1], matB[2])

        try:
            entityA.addWithAnother(entityB).matrix['data']
            return 0
        except rtp.badAddition:
            # badaddition correctly raised
            return 'badAddition correctly raised'

    def addVectors(self, matA, matB):

        entityA = entityB = None
        matA = json.loads(matA)
        matB = json.loads(matB)
        
        entityA = rtv.rtVector(matA[0], matA[1], matA[2])
        entityB = rtv.rtVector(matB[0], matB[1], matB[2])

        return entityA.addWithAnother(entityB).getMatrixData()

    def addPointToAVector(self, matA, matB):

        entityA = entityB = None
        matA = json.loads(matA)
        matB = json.loads(matB)
        
        entityA = rtp.rtPoint(matA[0], matA[1], matA[2])
        entityB = rtv.rtVector(matB[0], matB[1], matB[2])

        return entityA.addWithAnother(entityB).getMatrixData()

    def multiplyPointByScalar(self, matA, scalar):

        entityA = entityB = None
        matA = json.loads(matA)
        
        entityA = rtp.rtPoint(matA[0], matA[1], matA[2])

        try:
            entityA.multiplyByScalar(scalar)
            return 0
        except rtp.badScalarMultiplication:
            # badScalarMultiplication correctly raised
            return ('badScalarMultiplication correctly raised')

    def multiplyVectorByScalar(self, matA, scalar):

        entityA = entityB = None
        matA = json.loads(matA)
        
        entityA = rtv.rtVector(matA[0], matA[1], matA[2])

        return (entityA.multiplyByScalar(scalar).getMatrixData())

    def dividePointByScalar(self, matA, scalar):

        entityA = entityB = None
        matA = json.loads(matA)
        
        entityA = rtp.rtPoint(matA[0], matA[1], matA[2])

        try:
            entityA.divideByScalar(scalar)
            return 0
        except rtp.badScalarDivision:
            # badScalarDivsion correctly raised
            return ('badScalarDivision correctly raised')

    def divideVectorByScalar(self, matA, scalar):

        entityA = entityB = None
        matA = json.loads(matA)
        
        entityA = rtv.rtVector(matA[0], matA[1], matA[2])

        return (entityA.divideByScalar(scalar).getMatrixData())

    def magnitudeOfPoint(self, matA):

        entityA = entityB = None
        matA = json.loads(matA)
        
        entityA = rtp.rtPoint(matA[0], matA[1], matA[2])

        try:
            entityA.magnitude()
            return 0
        except rtp.badMagnitude:
            # badMagnitude correctly raised
            return ('badMagnitude correctly raised')

    def magnitudeOfVector(self, matA):

        entityA = entityB = None
        matA = json.loads(matA)
        
        entityA = rtv.rtVector(matA[0], matA[1], matA[2])

        return (entityA.magnitude())


    def normalisePoint(self, matA):

        entityA = entityB = None
        matA = json.loads(matA)
        
        entityA = rtp.rtPoint(matA[0], matA[1], matA[2])

        try:
            entityA.normalise()
            return 0
        except rtp.badNormalise:
            # badNormalise correctly raised
            return ('badNormalise correctly raised')

    def normaliseVector(self, matA):

        entityA = entityB = None
        matA = json.loads(matA)
        
        entityA = rtv.rtVector(matA[0], matA[1], matA[2])

        return (entityA.normalise().getMatrixData())

    def dotProductPoint(self, matA, matB):

        entityA = entityB = None
        matA = json.loads(matA)
        
        entityA = rtp.rtPoint(matA[0], matA[1], matA[2])
        entityB = rtp.rtPoint(matB[0], matB[1], matB[2])

        try:
            entityA.dotProductWithAnother(entityB)
            return 0
        except rtp.badDotProduct:
            # badDotProduct correctly raised
            return ('badDotProduct correctly raised')

    def dotProductVector(self, matA, matB):

        entityA = entityB = None
        matA = json.loads(matA)
        matB = json.loads(matB)
        
        entityA = rtv.rtVector(matA[0], matA[1], matA[2])
        entityB = rtv.rtVector(matB[0], matB[1], matB[2])

        return (entityA.dotProductWithAnother(entityB))

    def crossProductPoint(self, matA, matB):

        entityA = entityB = None
        matA = json.loads(matA)
        
        entityA = rtp.rtPoint(matA[0], matA[1], matA[2])
        entityB = rtp.rtPoint(matB[0], matB[1], matB[2])

        try:
            entityA.crossProductWithAnother(entityB)
            return 0
        except rtp.badCrossProduct:
            # badCrossProduct correctly raised
            return ('badCrossProduct correctly raised')

    def crossProductVector(self, matA, matB):

        entityA = entityB = None
        matA = json.loads(matA)
        matB = json.loads(matB)
        
        entityA = rtv.rtVector(matA[0], matA[1], matA[2])
        entityB = rtv.rtVector(matB[0], matB[1], matB[2])

        return (entityA.crossProductWithAnother(entityB))

    
        
if __name__== "__main__":

    ##  Testing scripts

    operation = sys.argv[1]
    matrix1 = sys.argv[2]

    if len(sys.argv) > 3:
        matrix2 = sys.argv[3]
    pvTester = pointsVectorsTester()
    if operation == 'testIsPoint':
        print (json.dumps(pvTester.runIsPoint(matrix1)))

    if operation == 'testIsVector':
        print (json.dumps(pvTester.runIsVector(matrix1)))

    if operation == 'addVectors':
        print (json.dumps(pvTester.addVectors(matrix1, matrix2)))

    if operation == 'addPoints':
        print (json.dumps(pvTester.addPoints(matrix1, matrix2)))

    if operation == 'addPointToAVector':
        print (json.dumps(pvTester.addPointToAVector(matrix1, matrix2)))

    if operation == 'multiplyPointByScalar':
        scalar = matrix2
        print (json.dumps(pvTester.multiplyPointByScalar(matrix1, scalar)))

    if operation == 'multiplyVectorByScalar':
        scalar = matrix2
        print (json.dumps(pvTester.multiplyVectorByScalar(matrix1, scalar)))

    if operation == 'dividePointByScalar':
        scalar = matrix2
        print (json.dumps(pvTester.dividePointByScalar(matrix1, scalar)))

    if operation == 'divideVectorByScalar':
        scalar = matrix2
        print (json.dumps(pvTester.divideVectorByScalar(matrix1, scalar)))

    if operation == 'magnitudeOfPoint':
        print (json.dumps(pvTester.magnitudeOfPoint(matrix1)))

    if operation == 'magnitudeOfVector':
        print (json.dumps(pvTester.magnitudeOfVector(matrix1)))

    if operation == 'normalisePoint':
        print (json.dumps(pvTester.normalisePoint(matrix1)))

    if operation == 'normaliseVector':
        print (json.dumps(pvTester.normaliseVector(matrix1)))

    if operation == 'dotProductPoint':
        print (json.dumps(pvTester.dotProductPoint(matrix1, matrix2)))

    if operation == 'dotProductVector':
        print (json.dumps(pvTester.dotProductVector(matrix1, matrix2)))

    if operation == 'crossProductPoint':
        print (json.dumps(pvTester.crossProductPoint(matrix1, matrix2)))

    if operation == 'crossProductVector':
        print (json.dumps(pvTester.crossProductVector(matrix1, matrix2)))



    
    

    

    
