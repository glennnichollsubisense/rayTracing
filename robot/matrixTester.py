import sys
import json

import matrices
import rtVector as rtv

class MatrixTester():

    def __init__(self):
        self.name = 'MatrixTester'


    def testIdentity(self, isHappyPath):

        # check a 4x4 matrix for an identity
        bMat = matrices.rtMatrix(4, 4)

        res = {}
        res['result'] = 'Fail'

        if isHappyPath:
            bMat.setRow (0, [1, 0, 0, 0])
            bMat.setRow (1, [0, 1, 0, 0])
            bMat.setRow (2, [0, 0, 1, 0])
            bMat.setRow (3, [0, 0, 0, 1])

            res['result'] = bMat.isIdentity()
            
        else:
            bMat.setRow (0, [-5, 2, 6, -8])
            bMat.setRow (1, [1, -5, 1, 8])
            bMat.setRow (2, [7, 7, -6, -7])
            bMat.setRow (3, [1, -3, 7, 4])

            res['result'] = bMat.isIdentity()

        print (json.dumps(res))

    def equality (self, matA, matB):

        entityA = entityB = None
        matA = json.loads(matA)
        matB = json.loads(matB)
        
        entityA = rtv.rtVector(matA[0], matA[1], matA[2])
        entityB = rtv.rtVector(matB[0], matB[1], matB[2])

        
        
if __name__== "__main__":

    ##  Testing scripts

    operation = sys.argv[1]

    if len(sys.argv) > 2:
        matrix1 = sys.argv[2]
    if len(sys.argv) > 3:
        matrix2 = sys.argv[3]

    mTester = MatrixTester()
    if operation == 'testIdentityFalse':
        mTester.testIdentity(False)

    elif operation == 'testIdentityTrue':
        mTester.testIdentity(True)

    elif operation == 'testEquality':
        print (json.dumps(mTester.equality(matrix1, matrix2)))

        
    
    

    

    
