from matrixTransformationFactory import rtMatrixTransformationFactory
from rtPoint import rtPoint
from rtRay import rtRay
from rtSphere import rtSphere
from rtVector import rtVector

from rtIntersection import rtIntersection, rtIntersectionSet

import canvas as cv
import colours as cl
from rtColourFactory import rtColourFactory
from pointLightSource import PointLightSource
from rtLighting import rtLighting

import cProfile

class sceneCreator(object):

    def runIt(self):
        ##  Testing scripts

        # make the backdrop canvas to receive the picture.
        # keep it small for now with just one object
        backPanelWidth = 200
        backPanelHeight = 200        
        aCanvas = cv.Canvas(backPanelWidth, backPanelHeight)
#        aCanvas.showMe(True)
        aCanvas.makeBlackCanvas()
        
        # make the object to be shown - a green sphere
        aSphere = rtSphere()
        aSphere.getMaterial().setTextBookGreen()

        # scale it but keep it on the origin
        tfac = rtMatrixTransformationFactory()
        aScaling = tfac.newScaling(50, 50, 50)
        aSphere.applyTransform(aScaling)

        # light source is a point source of white light
        # above, behind and to the left of the eye
        lightPoint = rtPoint(0, 0, -60)
        aLightSource = PointLightSource(None, lightPoint)

        # origin of the rays is where the eye is
        rayOrigin = rtPoint(0, 0, -100)


        
        startX = int((backPanelWidth/2) * -1.0)
        endX   = int((backPanelWidth/2))
        startY = int((backPanelHeight/2) * -1.0)
        endY   = int((backPanelHeight/2))
        
        xOffset = int(backPanelWidth/2)
        yOffset = int(backPanelHeight/2)


        interSet = rtIntersectionSet()
        
        rtf = rtColourFactory()
        for ix in range (startX, endX):
            for iy in range (startY, endY):

                interSet.clearIntersections()

                if ix==iy:
                    print ('%s-%s' % (str(ix), str(iy)))
                
                rayVector = rtVector (ix - rayOrigin.getMatrixData()[0][0], \
                                      iy - rayOrigin.getMatrixData()[0][1], \
                                      50 - rayOrigin.getMatrixData()[0][2]
                ).normalise()
                tRay = rtRay(rayOrigin, rayVector)
                intersections = tRay.intersectionsWithSphere(aSphere)
                if len(intersections) >0:

                    for iInter in intersections:
                        interSet.addIntersection (rtIntersection(iInter))

                    nearestInter = nearestIntersection = interSet.hit()

                    posOnSphere = tRay.position(nearestInter['tvalue'])
                    posX = posOnSphere.getMatrixData()[0][0]
                    posY = posOnSphere.getMatrixData()[0][1]
                    posZ = posOnSphere.getMatrixData()[0][2]


#                    posOnSphere.showMe('pos on sphere')
                    
                    eyeX = rayOrigin.getMatrixData()[0][0]
                    eyeY = rayOrigin.getMatrixData()[0][1]
                    eyeZ = rayOrigin.getMatrixData()[0][2]
                    
                    surfaceNormal = aSphere.normalAtWorldPoint (posX, posY, posZ).normalise()

                    tMaterial = aSphere.getMaterial()
                    tLightPoint = aLightSource
                    tPoint = posOnSphere
                    tEyeVector = rayOrigin.subtractAnotherFromMe(posOnSphere)

#                    tEyeVector.showMe()
                    

                    tNormalVector = surfaceNormal

#                    tNormalVector.showMe('surface normal')
                    
                    aLighting = rtLighting(tMaterial, tLightPoint, tPoint, tEyeVector, tNormalVector)
                    pixelColour = aLighting.getColour()['colour']

#                    print ('pixelColour %s ' % str(pixelColour))
                    
                    tColour = cl.rtColour(pixelColour[0], pixelColour[1], pixelColour[2])
                    try:
                        aCanvas.setPixel (ix + xOffset, iy + yOffset, tColour)
                    except cv.outOfCanvasBounds:
                        # print ('%s,%s out of bounds' % (str(ix), str(iy)))
                        pass

                    
        aCanvas.saveAs ('/home/pi/Projects/rayTracing-git/rayTracing/outputs/ch6ShadedGreenSphere.ppm')

if __name__== "__main__":


    aSceneCreator = sceneCreator()
    aSceneCreator.runIt()
#    cProfile.run ('aSceneCreator.runIt()')

    


