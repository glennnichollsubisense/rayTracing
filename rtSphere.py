import math

import rtPoint
from   rtPointFactory import rtPointFactory
import rtVector
from   matrixTransformationFactory import rtMatrixTransformationFactory
from   material import rtMaterial

class rtSphere(object):

    def __init__(self, pRadius=1.0, pOrigin=None, pID='1'):

        if pOrigin == None:
            tfac = rtPointFactory()
            self.sOrigin = tfac.newOriginPoint()
        else:            
            self.sOrigin = pOrigin

        self.sRadius = pRadius
        self.sObjectID = pID

        self.sMaterial = rtMaterial()
        self.sMaterial.setDefaultValues()
        
        self.sTransform = rtMatrixTransformationFactory().newIdentity()
        self.sInverseTransform = self.sTransform.inverse()

        delta = 0.00001
        if abs(pRadius - 1.0) > delta:
            self.sTransform = rtMatrixTransformationFactory().newScaling( pRadius, pRadius, pRadius )
            self.sInverseTransform = self.sTransform.inverse()
            

    def origin(self):
        return self.sOrigin
        
    def radius(self):
        return self.sRadius

    def transform(self):
        return self.sTransform

    def inverseTransform(self):
        return self.sInverseTransform

    def applyTransform(self, pTransform):

        self.sTransform = self.sTransform.transform (pTransform)
        self.sInverseTransform = self.sTransform.inverse()
        
    def setMaterial (self, pMaterial):
        self.sMaterial = pMaterial
        
    def getMaterial (self):
        return self.sMaterial
        
    def asText(self):
        return 'Sphere %s' % str(self.sObjectID)
    
    def normalAtObjectPoint(self, objectX, objectY, objectZ):

        # return a vector from my centre to the point objectX, objectY, objectZ
        originData = self.sOrigin.getMatrixData()

        return rtVector.rtVector(objectX - originData[0][0], objectY - originData[0][1], objectZ - originData[0][2])

    def normalAtWorldPoint(self, worldX, worldY, worldZ):

        # return a vector from my centre to the world point worldX, worldY, worldZ

        # object point is  the point transformed to object space
        # objectPoint = inverse(self.transform) * world point

        worldPoint = rtPoint.rtPoint(worldX, worldY, worldZ)

        objectPointMatrix = self.transform().inverse().multiplyWithAnother(worldPoint.matrix.transpose()).transpose()
        objectPoint = rtPoint.rtPoint()
        objectPoint.matrix = objectPointMatrix

        objectNormal = objectPoint.subtractAnotherFromMe(rtPoint.rtPoint())

        worldNormalMatrix = self.transform().inverse().transpose().multiplyWithAnother(objectNormal.matrix.transpose()).transpose()

        worldNormal = rtVector.rtVector()
        worldNormal.matrix = worldNormalMatrix

        return worldNormal


    
    def showMe(self, label=''):

        if len(label) > 0:
            print ('**** %s ****' % label)
        print ('origin')
        self.sOrigin.showMe()
        print ('radius %s' % str(self.sRadius))
        self.sTransform.showMe('Transform')
        self.sMaterial.showMe('Material')
        

    def asDictionary(self):

        res = {'Sphere': {}}
        res['Sphere']['origin'] = self.origin().asDictionary()
        res['Sphere']['radius'] = self.radius()
        res['Sphere']['id'] = self.sObjectID
        return res

        
