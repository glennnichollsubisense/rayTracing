import math

import rtVector
import rtPoint
import rtSphere

class rtRay(object):

    def __init__(self, pOrigin=None, pDirection=None):
        self.sOrigin = pOrigin
        self.sDirection = pDirection

    def setFromArrays(self, arryPoint, arryVector):
        self.sOrigin = rtPoint.rtPoint(arryPoint[0], arryPoint[1], arryPoint[2])
        self.sDirection = rtVector.rtVector(arryVector[0], arryVector[1], arryVector[2])

    def origin(self):
        return self.sOrigin

    def direction(self):
        return self.sDirection

    def position(self, pT):

        # compute the length of the vector
        x = self.direction().getValue(0, 0)
        y = self.direction().getValue(0, 1)
        z = self.direction().getValue(0, 2)

        length= math.sqrt((x*x) + (y*y) + (z*z))

        newX = ((x * pT) / length ) + self.origin().getValue(0, 0)
        newY = ((y * pT) / length ) + self.origin().getValue(0, 1)
        newZ = ((z * pT) / length ) + self.origin().getValue(0, 2)

        resPt = rtPoint.rtPoint(newX, newY, newZ)
        return resPt
        

    def intersectionsWithSphere (self, pSphere):

        a = self.sDirection.dotProductWithAnother(self.sDirection)

        sphereToRay= rtVector.rtVector(self.sOrigin.getValue(0, 0) - pSphere.origin().getValue(0, 0), \
                                       self.sOrigin.getValue(0, 1) - pSphere.origin().getValue(0, 1), \
                                       self.sOrigin.getValue(0, 2) - pSphere.origin().getValue(0, 2), \
                                      )
        b = 2 * (self.sDirection.dotProductWithAnother(sphereToRay))
        c = sphereToRay.dotProductWithAnother(sphereToRay) - 1

        discriminant = (b*b) - (4 * a * c)

        if discriminant<0:
            # No intersection
            return ()

        # figure out the 2 versions of t that intersect the sphere
        t1 = ((b * -1) - math.sqrt(discriminant)) / (2 * a)
        t2 = ((b * -1) + math.sqrt(discriminant)) / (2 * a)

        return (t1, t2)

    def translate(self, translation):
        
        coords = self.sOrigin.multiplyWithAnother(translation)
        newOrigin = rtPoint.rtPoint()
        print ('^^^^ coords = %s' % str(coords))
        newOrigin.setFromMatrix(coords)
        newOrigin.showMe(False, 'newOrigin of ray')
        
        newVector = rtVector.rtVector(self.sDirection)
        tRay = rtRay(newOrigin.matrix['data'], newVector.matrix['data'])
        return tRay

        
    

    def showMe(self):
        print ('*** Ray ***')
#        print ('origin %s' % str(self.sOrigin.matrix['data']))
#        print ('direction %s' % str(self.sDirection.matrix['data']))
        print ('origin %s' % str(self.sOrigin))
        print ('direction %s' % str(self.sDirection))
