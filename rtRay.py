import math

import rtVector
import rtPoint
import rtSphere
import rtWorld
import rtIntersection

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
        x = self.direction().matrix.getValue(0, 0)
        y = self.direction().matrix.getValue(0, 1)
        z = self.direction().matrix.getValue(0, 2)

        length= math.sqrt((x*x) + (y*y) + (z*z))

        newX = ((x * pT) / length ) + self.origin().matrix.getValue(0, 0)
        newY = ((y * pT) / length ) + self.origin().matrix.getValue(0, 1)
        newZ = ((z * pT) / length ) + self.origin().matrix.getValue(0, 2)

        resPt = rtPoint.rtPoint(newX, newY, newZ)
        return resPt
        

    def intersectionsWithSphere (self, pSphere):

        # to get the intersections with a transformed sphere, first transform
        # myself with the inverse of the sphere's transform
        inverseSphereTransform = pSphere.inverseTransform()

        adjustedRay = self.generalTransform(inverseSphereTransform)
        
        
        a = adjustedRay.sDirection.dotProductWithAnother(adjustedRay.sDirection)

        sphereToRay= rtVector.rtVector(adjustedRay.sOrigin.matrix.getValue(0, 0), \
                                       adjustedRay.sOrigin.matrix.getValue(0, 1), \
                                       adjustedRay.sOrigin.matrix.getValue(0, 2), \
                                      )
        b = 2 * (adjustedRay.sDirection.dotProductWithAnother(sphereToRay))
        c = sphereToRay.dotProductWithAnother(sphereToRay) - 1

        discriminant = (b*b) - (4 * a * c)

        if discriminant<0:
            # No intersection
            return ()

        # figure out the 2 values of t that intersect the sphere
        t1 = ((b * -1) - math.sqrt(discriminant)) / (2 * a)
        t2 = ((b * -1) + math.sqrt(discriminant)) / (2 * a)

        return (t1, t2)

    def detailedIntersectionWithShape (self, pShape, pTValue):

        # Returns a whole pile of information about the intersection
        # Just works for spheres at the moment but will be expanded to include other shapes

        res = {}
        interSet = rtIntersection.rtIntersectionSet()
        intersections = self.intersectionsWithSphere (pShape)

        if len(intersections)==0:
            return res
        
        for iInter in intersections:
            interSet.addIntersection (rtIntersection.rtIntersection(iInter))

        res['t'] = interSet.hit()
        res['object'] = pShape

        posOnSphere = self.position(res['t']['tvalue'])
        res['point'] = posOnSphere
        res['eyev'] = self.direction()

        posX = posOnSphere.getMatrixData()[0][0]
        posY = posOnSphere.getMatrixData()[0][1]
        posZ = posOnSphere.getMatrixData()[0][2]
        
        res['normalv'] = pShape.normalAtWorldPoint (posX, posY, posZ).normalise()

        # figure out if the normal vector is pointing away from us
        # this happens when the eye is inside a shape
        
        # The book says the vector is inside if the dot product < 0.0
        # but that cannot be right.  If the dot product is < 0.0 it means the vectors
        # are pointing in different directions, which is  the case if the eye vector is outside the shape
        # if the eye vector is inside the shape the normal vector points in the same direction, so the
        # dot product is > 0
        res['inside'] = False
        if float(res['normalv'].dotProductWithAnother(res['eyev'])) > 0.0:
            res['inside'] = True
            res['normalv'] = res['normalv'].negate()
            
        return res
        

    def intersectionsWithWorld (self, pWorld):

        intersections = []
        for iobject in pWorld.getObjects():
            intersections.extend (self.intersectionsWithSphere(iobject))

        intersections.sort()
        return intersections
    
    def generalTransform (self, transform):
        newOrigin = self.sOrigin.generalTransform(transform)        
        newDirection = self.sDirection.generalTransform(transform)
        return rtRay(newOrigin, newDirection)
    
    def translate(self, translation):
        
        newOrigin = self.sOrigin.translate(translation)        
        newDirection = self.sDirection
        return rtRay(newOrigin, newDirection)
    
    def scale(self, scaling):
        return self.generalTransform(scaling)
    

    def showMe(self, name=None):

        if name==None:
            name=''            
        print ('*** Ray %s ***' % name)
        print ('origin')
        self.sOrigin.showMe()
        print ('direction')
        self.sDirection.showMe()
