
class expected2x2(Exception):

    def __init__(self, message):
        super(expected2x2, self).__init__(message)

class expected3x3(Exception):

    def __init__(self, message):
        super(expected3x3, self).__init__(message)

class badMatrixShape(Exception):

    def __init__(self, message):
        super(badMatrixShape, self).__init__(message)

class outOfMatrixBounds(Exception):

    def __init__(self, message):
        super(outOfMatrixBounds, self).__init__(message)

class matrixNotInvertible(Exception):

    def __init__(self, message):
        super(matrixNotInvertible, self).__init__(message)


class rtMatrix(object):

    def __init__(self, height, width, identity=False):

        self.matrix = {}
        self.matrix['width'] = width
        self.matrix['height'] = height
        self.matrix['data'] = [0] * height 
        for iheight in range (0, height):
            self.matrix['data'][iheight] = [0.0] * width


        if identity == True:
            if self.width() != self.height():
                raise (badMatrixShape ('need width and height to be the same for an identity matrix'))

            for iheight in range(0, self.height()):
                self.matrix['data'][iheight] = [0] * self.width()

            for ivalue in range(0, self.height()):
                self.matrix['data'][ivalue][ivalue] = 1.0

    def width(self):
        return self.matrix['width']
    
    def height(self):
        return self.matrix['height']
    
    def fpAEqualsB (self, a, b):

        delta = 0.0001
        return abs (a-b) < delta

    
    def setValue (self, y, x, value):

        if (x<0) or (x>=self.width()):
            raise (outOfMatrixBounds('out of bounds'))
        if (y<0) or (y>=self.height()):
            raise (outOfMatrixBounds('out of bounds'))
        
        self.matrix['data'][y][x] = value

    def setRow(self, rowNo, values):
        
        for i in range (0, len(values)):
            self.setValue(rowNo, i, values[i])

    def setColumn(self, columnNo, values):
        
        for i in range (0, len(values)):
            self.setValue(i, columnNo, values[i])

    def getValue (self, y, x):

        if (x<0) or (x>=self.width()):
            raise (outOfMatrixBounds('out of bounds'))
        if (y<0) or (y>=self.height()):
            raise (outOfMatrixBounds('out of bounds'))

        return self.matrix['data'][y][x]

    def compareWithAnother (self, another):

        if self.width() != another.width():
            return False
        if self.height() != another.height():
            return False

        for iheight in range(0, self.height()):
            for iwidth in range(0, self.width()):
                if self.matrix['data'][iheight][iwidth] != another.matrix['data'][iheight][iwidth]:
                    return False
        return True


    def addWithAnother(self, another):

        if self.width() != another.width():
            raise badMatrixShape('matrices need to be the same width to add them')
        if self.height() != another.height():
            raise badMatrixShape('matrices need to be the same height to add them')

        resMatrix = rtMatrix(self.height(), self.width())
        for iheight in range (0, self.height()):
            for iwidth in range (0, self.width()):
                tSum = self.getValue(iheight, iwidth) + another.getValue(iheight, iwidth)
                resMatrix.setValue(iheight, iwidth, tSum)
        return resMatrix
        

    def subtractFromMe(self, another):

        if self.width() != another.width():
            raise badMatrixShape('matrices need to be the same width to subtract them')
        if self.height() != another.height():
            raise badMatrixShape('matrices need to be the same height to subtract them')

        resMatrix = rtMatrix(self.height(), self.width())
        for iheight in range (0, self.height()):
            for iwidth in range (0, self.width()):
                tDiff = self.getValue(iheight, iwidth) - another(iheight, iwidth)
                resMatrix.setValue(iheight, iwidth, tDiff)
        return resMatrix
        
    def multiplyByScalar(self, scalar):

        resMatrix = rtMatrix(self.height(), self.width())
        for iheight in range (0, self.height()):
            for iwidth in range (0, self.width()):
                tMultByScalar = float(self.getValue(iheight, iwidth)) * float(scalar)
                resMatrix.setValue(iheight, iwidth, tMultByScalar)
        return resMatrix

    def divideByScalar(self, scalar):

        resMatrix = rtMatrix(self.height(), self.width())
        for iheight in range (0, self.height()):
            for iwidth in range (0, self.width()):
                tDivByScalar = float(self.getValue(iheight, iwidth)) / float(scalar)
                resMatrix.setValue(iheight, iwidth, tDivByScalar)
        return resMatrix



    def transform (self, another):
        return self.multiplyWithAnother (another)
    
    def multiplyWithAnother(self, another):

        # need (RxC) of self to be able to multiply with (RxC) of another
        # so self.C must equal another.R

        if self.width() != another.height():
            raise (badMatrixShape, 'matrices cannot be multiplied')

        resMatrix = rtMatrix(self.height(), another.width())

        for iheight in range (0, self.height()):
            for iwidth in range (0, another.width()):
                total = 0
                for ictr in range (0, self.width()):
                    total = total + self.matrix['data'][iheight][ictr] * another.matrix['data'][ictr][iwidth]


                resMatrix.setValue(iheight, iwidth, total) 

        return resMatrix
    

    def transpose(self):

        # convert a mxn matrix to a nxm matrix

        resMatrix = rtMatrix(self.width(), self.height())

        for iheight in range (0, self.height()):
            for iwidth in range (0, self.width()):
                resMatrix.setValue(iwidth, iheight, self.getValue(iheight, iwidth))

        return resMatrix
    


    def determinant(self):

        if self.width() != self.height():
            raise (badMatrixShape, 'need a square matrix to do a determinant')
            
        if self.width() == 1:
            raise (badMatrixShape, 'need a matrix bigger than 1x1 to do a determinant')
            
        if self.width() == 2 and self.height() == 2:
        
            leading = self.getValue(0, 0) * self.getValue(1,1)
            trailing = self.getValue(0, 1) * self.getValue(1,0)
            return leading - trailing

        else:
            runningDeterminant = 0
            for i in range (0, self.width()):
                runningDeterminant = runningDeterminant + (self.getValue(0, i) * self.cofactor(0, i))

            return runningDeterminant

        
    def subMatrix(self, row, column):

        if (self.height()< 2) or (self.width()< 2):
            raise(badMatrixShape, 'need at least 2 rows and 2 columns to take a submatrix')

        resMatrix = rtMatrix(self.height()-1, self.width()-1)

        rowTriggered = False
        for iheight in range (0, self.height()):
            colTriggered = False
            for iwidth in range (0, self.width()):

                if iheight == row:
                    rowTriggered = True
                    continue
                if iwidth == column:
                    colTriggered = True
                    continue

                trow = iheight
                if rowTriggered == True:
                    trow = iheight-1
                tcol = iwidth
                if colTriggered == True:
                    tcol = iwidth-1

                resMatrix.setValue(trow, tcol, self.getValue(iheight, iwidth))

        return resMatrix

    def minor(self, row, column):
        return self.subMatrix(row, column).determinant()

    def cofactor(self, row, column):

        
        minor = self.minor(row, column)

        # figure out if we need to negate the answer
        if ((row + column) % 2) != 0:
            return (minor * -1)

        return minor

    def isInvertible (self):

        if fpAEqualsB(self.determinant, 0):
            raise matrixNotInvertible ('matrix is not invertible')

        return True

    def isIdentity (self):

        if self.height() != self.width():
            raise badMatrixShape ('need a square matrix for identity test')

        for iheight in range(0, self.height()):
            for iwidth in range(0, self.width()):
                if iheight == iwidth:
                    if self.fpAEqualsB (self.getValue(iheight, iwidth), 1.0)  == False:
                        return False
                else:
                    if self.fpAEqualsB (self.getValue(iheight, iwidth), 0.0)  == False:
                        return False

        return True

    
    def inverse (self):

        tDeterminant = self.determinant()
        inverseMatrix = rtMatrix(self.height(), self.width())
        for iheight in range (0, self.height()):
            for iwidth in range (0, self.width()):
                inverseMatrix.setValue(iheight, iwidth, self.cofactor(iheight, iwidth) / float(tDeterminant))

        resMatrix = inverseMatrix.transpose()  # GNGN dont do this.  dont change the original

        return resMatrix
        

        
    def showMe(self, short=False, title=''):

        print ('%s --- Matrix %i x %i ' % (title, self.height(), self.width()))
        
        if short == True:
            return 

        for iheight in range (0, self.height()):

            rowStr = ''            
            for iwidth in range (0, self.width()):
                rowStr = rowStr + ' %s ' % str(float(self.matrix['data'][iheight][iwidth]))

            print ('[ ' + rowStr + ']')



if __name__== "__main__":

    ##  Testing scripts

    print (' ^^^ Testing the matrices')

    mat = rtMatrix(5, 5, True)
    mat.showMe()

    aMat = rtMatrix(3, 3, True)
    aMat.setValue (0, 0, 3.0)
    aMat.setValue (0, 1, 4.0)
    aMat.setValue (0, 2, 5.0)
    aMat.showMe()


    bMat = rtMatrix(3, 3, True)
    bMat.setValue (0, 0, 3.0)
    bMat.setValue (0, 1, 4.0)
    bMat.setValue (0, 2, 5.0)
    print ('comparison %s' % str(aMat.compareWithAnother(bMat)))
    
    bMat.setValue (0, 2, 5.5)
    print ('comparison %s' % str(aMat.compareWithAnother(bMat)))

    
    aMat = rtMatrix(3, 5)
    aMat.setValue (0, 0, 3.0)
    aMat.setValue (0, 1, 4.0)
    aMat.setValue (0, 2, 5.0)
    aMat.showMe()

    print ('multiplication')

    aMat = rtMatrix(2, 2)
    aMat.setValue (0, 0, 3.0)
    aMat.setValue (0, 1, 4.0)
    aMat.setValue (1, 0, 5.0)
    aMat.setValue (1, 1, 6.0)
    aMat.showMe()

    bMat = rtMatrix(2, 2)
    bMat.setValue (0, 0, 3.0)
    bMat.setValue (0, 1, 4.0)
    bMat.setValue (1, 0, 5.0)
    bMat.setValue (1, 1, 6.0)
    bMat.showMe()

    resMat = aMat.multiplyWithAnother(bMat)
    resMat.showMe()

    aMat = rtMatrix(2, 3)
    aMat.setValue (0, 0, 5.0)
    aMat.setValue (0, 1, 10.0)
    aMat.setValue (0, 2, 15.0)
    aMat.setValue (1, 0, 6.0)
    aMat.setValue (1, 1, 7.0)
    aMat.setValue (1, 2, 8.0)
    aMat.showMe()

    bMat = rtMatrix(3, 2)
    bMat.setValue (0, 0, 1.0)
    bMat.setValue (0, 1, 2.0)
    bMat.setValue (1, 0, 3.0)
    bMat.setValue (1, 1, 4.0)
    bMat.setValue (2, 0, 5.0)
    bMat.setValue (2, 1, 6.0)
    bMat.showMe()

    resMat = aMat.multiplyWithAnother(bMat)
    resMat.showMe()

    
    aMat = rtMatrix(1, 3)
    aMat.setValue (0, 0, 5.0)
    aMat.setValue (0, 1, 10.0)
    aMat.setValue (0, 2, 15.0)
    aMat.showMe()

    bMat = rtMatrix(3, 1)
    bMat.setValue (0, 0, 1.0)
    bMat.setValue (1, 0, 3.0)
    bMat.setValue (2, 0, 5.0)
    bMat.showMe()

    resMat = aMat.multiplyWithAnother(bMat)
    resMat.showMe()

    # transpose
    aMat = rtMatrix(1, 3)
    aMat.setValue (0, 0, 5.0)
    aMat.setValue (0, 1, 10.0)
    aMat.setValue (0, 2, 15.0)
    aMat.showMe(False, 'Transposing')

    resMatrix = aMat.transpose()
    resMatrix.showMe(False, 'Transposed')


    bMat = rtMatrix(3, 2)
    bMat.setValue (0, 0, 1.0)
    bMat.setValue (0, 1, 2.0)
    bMat.setValue (1, 0, 3.0)
    bMat.setValue (1, 1, 4.0)
    bMat.setValue (2, 0, 5.0)
    bMat.setValue (2, 1, 6.0)
    bMat.showMe(False, 'Transposing')

    resMat = bMat.transpose()
    resMat.showMe(False, 'Transposed')

                                   
    # determinant
    bMat = rtMatrix(2, 2)
    bMat.setValue (0, 0, 6.0)
    bMat.setValue (0, 1, 8.0)
    bMat.setValue (1, 0, 10.0)
    bMat.setValue (1, 1, 12.0)
    bMat.showMe(False, 'Determinant')

    print ('determinant = %s ' % str(bMat.determinant()))

    # submatrix
    bMat = rtMatrix(3, 3)
    bMat.setValue (0, 0, 2.0)
    bMat.setValue (0, 1, 4.0)
    bMat.setValue (0, 2, 6.0)
    bMat.setValue (1, 0, 8.0)
    bMat.setValue (1, 1, 10.0)
    bMat.setValue (1, 2, 12.0)
    bMat.setValue (2, 0, 14.0)
    bMat.setValue (2, 1, 16.0)
    bMat.setValue (2, 2, 18.0)
    bMat.showMe(False, 'Subclassing this')

    resMatrix = bMat.subMatrix(1, 1)
    resMatrix.showMe(False, 'Subclassed')
    
    resMatrix = bMat.subMatrix(0, 0)
    resMatrix.showMe(False, 'Subclassed')

    resMatrix = bMat.subMatrix(0, 2)
    resMatrix.showMe(False, 'Subclassed')
    

    # minor
    bMat = rtMatrix(3, 3)
    bMat.setValue (0, 0, 2.0)
    bMat.setValue (0, 1, 4.0)
    bMat.setValue (0, 2, 6.0)
    bMat.setValue (1, 0, 8.0)
    bMat.setValue (1, 1, 10.0)
    bMat.setValue (1, 2, 12.0)
    bMat.setValue (2, 0, 14.0)
    bMat.setValue (2, 1, 16.0)
    bMat.setValue (2, 2, 18.0)
    bMat.showMe(False, 'Finding the minor of  this')

    print ('Minor is %s ' % str(bMat.minor(1, 1)))

    # cofactor
    bMat = rtMatrix(3, 3)
    bMat.setValue (0, 0, 3.0)
    bMat.setValue (0, 1, 5.0)
    bMat.setValue (0, 2, 0.0)
    bMat.setValue (1, 0, 2.0)
    bMat.setValue (1, 1, -1.0)
    bMat.setValue (1, 2, -7.0)
    bMat.setValue (2, 0, 6.0)
    bMat.setValue (2, 1, -1.0)
    bMat.setValue (2, 2, 5.0)
    bMat.showMe(False, 'Finding the cofactor of  this')

    print ('minor of 0,0 is %s ' % str(bMat.minor(0, 0)))
    print ('minor of 1,0 is %s ' % str(bMat.minor(1, 0)))
    print ('cofactor of 0,0 is %s ' % str(bMat.cofactor(0, 0)))
    print ('cofactor of 1,0 is %s ' % str(bMat.cofactor(1, 0)))


    # determinant of 3x3 matrix
    bMat = rtMatrix(3, 3)
    bMat.setRow (0, [1, 2, 6])
    bMat.setRow (1, [-5, 8, -4])
    bMat.setRow (2, [2, 6, 4])
    print ('determinant of 3x3 = %s ' % str(bMat.determinant()) )
    
    # determinant of 4x4 matrix
    bMat = rtMatrix(4, 4)
    bMat.setRow (0, [-2, -8, 3, 5])
    bMat.setRow (1, [-3, 1, 7, 3])
    bMat.setRow (2, [1, 2, -9, 6])
    bMat.setRow (3, [-6, 7, 7, -9])
    print ('determinant of 4x4 = %s ' % str(bMat.determinant()) )
    
    # inverse of 4x4 matrix
    bMat = rtMatrix(4, 4)
    bMat.setRow (0, [-5, 2, 6, -8])
    bMat.setRow (1, [1, -5, 1, 8])
    bMat.setRow (2, [7, 7, -6, -7])
    bMat.setRow (3, [1, -3, 7, 4])

    inverseMatrix = bMat.inverse()
    inverseMatrix.showMe (False, 'Inverse of the matrix')
    
    resMatrix = bMat.multiplyWithAnother(inverseMatrix)
    resMatrix.showMe (False, 'multiply with the inverse')
    print('should be an identity matrix %s' % resMatrix.isIdentity())

    # 2nd inverse of 4x4 matrix test
    bMat = rtMatrix(4, 4)
    bMat.setRow (0, [8, -5, 9, 2])
    bMat.setRow (1, [7, 5, 6, 1])
    bMat.setRow (2, [-6, 0, 9, 6])
    bMat.setRow (3, [-3, 0,-9, -4])

    inverseMatrix = bMat.inverse()
    inverseMatrix.showMe (False, '2nd Inverse test')
    
    # 3rd inverse of 4x4 matrix test
    bMat = rtMatrix(4, 4)
    bMat.setRow (0, [9, 3, 0, 9])
    bMat.setRow (1, [-5, -2, -6, -3])
    bMat.setRow (2, [-4, 9, 6, 4])
    bMat.setRow (3, [-7, 6, 6, 2])

    inverseMatrix = bMat.inverse()
    inverseMatrix.showMe (False, '3rd Inverse test')
    
    
