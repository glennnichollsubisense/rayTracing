import colours
from colours import rtColour
from rtColourFactory import rtColourFactory
import material
import pointLightSource
import rtPoint
import rtVector


class rtLighting(object):

    def __init__(self, pMaterial, pLightPoint, pPoint, pEyeVector, pNormalVector):

        
        self.sMaterial = pMaterial
        self.sLightPoint = pLightPoint
        self.sPoint = pPoint
        self.sEyeVector = pEyeVector
        self.sNormalVector = pNormalVector


    def getColour(self):


        effectiveColour = self.sMaterial.getColour().multiplyByAnother(self.sLightPoint.getColour())

        lightVector = self.sLightPoint.getPoint().subtractAnotherFromMe(self.sPoint).normalise()
        ambient = effectiveColour.multiplyByScalar(self.sMaterial.getAmbient())

        lightDotNormal = lightVector.dotProductWithAnother(self.sNormalVector)
        rtf = rtColourFactory()
        diffuse = rtf.newBlack()
        specular = rtf.newBlack()

        if lightDotNormal >= 0.0:


            try:
                diffuse = effectiveColour.multiplyByScalar(self.sMaterial.getDiffuse())
                diffuse = diffuse.multiplyByScalar(lightDotNormal)
                reflectVector = lightVector.negate().reflectWithAnother(self.sNormalVector)
                reflectDotEye = reflectVector.dotProductWithAnother(self.sEyeVector)
                if reflectDotEye <= 0:
                    specular = rtf.newBlack()
                else:       
                    factor = pow(reflectDotEye, self.sMaterial.getShininess())
                    specular = self.sLightPoint.getColour().multiplyByScalar(self.sMaterial.getSpecular())
                    specular = specular.multiplyByScalar(factor)
            except Exception:
                print ('Exception went off in rtLighting.getColour()')
                specular = rtf.newRed()

        colour = ambient.addB(diffuse)
        colour = colour.addB(specular)
                
        return {'colour': colour.getRGB()}
    
            
